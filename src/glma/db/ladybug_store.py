"""Ladybug graph database store for code chunks and file records."""

from pathlib import Path
from typing import Optional

from real_ladybug import Database, Connection

from glma.models import Chunk, FileRecord, Relationship


class LadybugStore:
    """Manages the Ladybug database for glma index storage."""

    SCHEMA_CHUNKS = """
    CREATE NODE TABLE IF NOT EXISTS Chunk (
        id STRING,
        file_path STRING,
        chunk_type STRING,
        name STRING,
        content STRING,
        summary STRING,
        start_line INT64,
        end_line INT64,
        content_hash STRING,
        parent_id STRING,
        PRIMARY KEY (id)
    )
    """

    SCHEMA_FILES = """
    CREATE NODE TABLE IF NOT EXISTS File (
        path STRING,
        language STRING,
        content_hash STRING,
        last_indexed STRING,
        chunk_count INT64,
        PRIMARY KEY (path)
    )
    """

    SCHEMA_CONTAINS = """
    CREATE REL TABLE IF NOT EXISTS CONTAINS (FROM File TO Chunk)
    """

    SCHEMA_RELATES_TO = """
    CREATE REL TABLE IF NOT EXISTS RELATES_TO (FROM Chunk TO Chunk, rel_type STRING, confidence STRING, source_line INT64, target_name STRING)
    """

    def __init__(self, db_path: Path):
        """Initialize store, creating/opening the database and ensuring schema exists.

        Args:
            db_path: Path to the database file. Parent directory will be created if needed.
        """
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.db = Database(str(db_path))
        self.conn = Connection(self.db)
        self._init_schema()

    def _init_schema(self) -> None:
        """Create tables if they don't exist."""
        self.conn.execute(self.SCHEMA_CHUNKS)
        self.conn.execute(self.SCHEMA_FILES)
        self.conn.execute(self.SCHEMA_CONTAINS)
        self.conn.execute(self.SCHEMA_RELATES_TO)

    def upsert_file(self, record: FileRecord) -> None:
        """Insert or update a file record. Uses detach delete+re-insert pattern."""
        # First delete chunks and their edges for this file
        self.conn.execute(
            "MATCH (c:Chunk {file_path: $fp}) DETACH DELETE c",
            {"fp": record.path},
        )
        # Then delete the file node (now safe since edges are gone)
        self.conn.execute(
            "MATCH (f:File {path: $path}) DELETE f",
            {"path": record.path},
        )
        data = record.model_dump()
        data["language"] = data["language"].value  # Serialize enum to string
        self.conn.execute(
            """CREATE (f:File {
                path: $path,
                language: $language,
                content_hash: $content_hash,
                last_indexed: $last_indexed,
                chunk_count: $chunk_count
            })""",
            data,
        )

    def upsert_chunks(self, file_path: str, chunks: list[Chunk]) -> None:
        """Delete existing chunks for a file and insert new ones."""
        # Remove old chunks and their CONTAINS edges
        self.conn.execute(
            "MATCH (c:Chunk {file_path: $fp}) DETACH DELETE c",
            {"fp": file_path},
        )
        # Insert new chunks
        for chunk in chunks:
            data = chunk.model_dump()
            # Serialize enums and handle None values
            data["chunk_type"] = data["chunk_type"].value
            # Ladybug doesn't accept None - use empty string for nullable fields
            data["summary"] = data.get("summary") or ""
            data["parent_id"] = data.get("parent_id") or ""
            self.conn.execute(
                """CREATE (c:Chunk {
                    id: $id,
                    file_path: $file_path,
                    chunk_type: $chunk_type,
                    name: $name,
                    content: $content,
                    summary: $summary,
                    start_line: $start_line,
                    end_line: $end_line,
                    content_hash: $content_hash,
                    parent_id: $parent_id
                })""",
                data,
            )
        # Create CONTAINS edges
        if chunks:
            self.conn.execute(
                """MATCH (f:File {path: $fp}), (c:Chunk {file_path: $fp})
                CREATE (f)-[:CONTAINS]->(c)""",
                {"fp": file_path},
            )

    def get_file_hash(self, file_path: str) -> Optional[str]:
        """Get stored content hash for a file, or None if not indexed."""
        result = self.conn.execute(
            "MATCH (f:File {path: $path}) RETURN f.content_hash",
            {"path": file_path},
        )
        rows = list(result)
        return rows[0][0] if rows else None

    def get_indexed_files(self) -> dict[str, str]:
        """Get all indexed file paths and their content hashes."""
        result = self.conn.execute("MATCH (f:File) RETURN f.path, f.content_hash")
        rows = list(result)
        return {row[0]: row[1] for row in rows}

    def delete_file(self, file_path: str) -> None:
        """Delete a file and all its chunks."""
        self.conn.execute(
            "MATCH (c:Chunk {file_path: $fp}) DETACH DELETE c",
            {"fp": file_path},
        )
        self.conn.execute(
            "MATCH (f:File {path: $path}) DELETE f",
            {"path": file_path},
        )

    def delete_relationships(self, file_path: str) -> None:
        """Delete all outgoing relationships from a file's chunks."""
        self.conn.execute(
            "MATCH (c:Chunk {file_path: $fp})-[r:RELATES_TO]->() DELETE r",
            {"fp": file_path},
        )

    def upsert_relationships(self, file_path: str, relationships: list[Relationship]) -> None:
        """Replace all outgoing relationships for a file's chunks."""
        self.delete_relationships(file_path)
        for rel in relationships:
            if rel.target_id:
                self.conn.execute(
                    """MATCH (src:Chunk {id: $sid}), (tgt:Chunk {id: $tid})
                    CREATE (src)-[:RELATES_TO {rel_type: $rt, confidence: $conf, source_line: $sl, target_name: $tn}]->(tgt)""",
                    {
                        "sid": rel.source_id,
                        "tid": rel.target_id,
                        "rt": rel.rel_type.value,
                        "conf": rel.confidence.value,
                        "sl": rel.source_line,
                        "tn": rel.target_name,
                    },
                )
            else:
                # Unresolved: store with source pointing to itself, target_name captures what was called
                self.conn.execute(
                    """MATCH (src:Chunk {id: $sid})
                    CREATE (src)-[:RELATES_TO {rel_type: $rt, confidence: $conf, source_line: $sl, target_name: $tn}]->(src)""",
                    {
                        "sid": rel.source_id,
                        "rt": rel.rel_type.value,
                        "conf": rel.confidence.value,
                        "sl": rel.source_line,
                        "tn": rel.target_name,
                    },
                )

    def get_outgoing_relationships(self, chunk_id: str) -> list[dict]:
        """Get all outgoing relationships from a chunk."""
        result = self.conn.execute(
            "MATCH (c:Chunk {id: $cid})-[r:RELATES_TO]->(t:Chunk) RETURN r.rel_type, r.confidence, r.source_line, r.target_name, t.id, t.name",
            {"cid": chunk_id},
        )
        rows = []
        for row in result:
            rows.append({
                "rel_type": row[0], "confidence": row[1], "source_line": row[2],
                "target_name": row[3], "target_id": row[4], "target_chunk_name": row[5],
            })
        return rows

    def get_incoming_relationships(self, chunk_id: str) -> list[dict]:
        """Get all incoming relationships to a chunk."""
        result = self.conn.execute(
            "MATCH (s:Chunk)-[r:RELATES_TO]->(c:Chunk {id: $cid}) RETURN r.rel_type, r.confidence, r.source_line, r.target_name, s.id, s.name",
            {"cid": chunk_id},
        )
        rows = []
        for row in result:
            rows.append({
                "rel_type": row[0], "confidence": row[1], "source_line": row[2],
                "target_name": row[3], "source_id": row[4], "source_chunk_name": row[5],
            })
        return rows

    def get_file_relationships(self, file_path: str) -> list[dict]:
        """Get all outgoing relationships from all chunks in a file."""
        result = self.conn.execute(
            "MATCH (c:Chunk {file_path: $fp})-[r:RELATES_TO]->(t:Chunk) RETURN c.id, c.name, r.rel_type, r.confidence, r.source_line, r.target_name, t.id, t.name",
            {"fp": file_path},
        )
        rows = []
        for row in result:
            rows.append({
                "source_id": row[0], "source_name": row[1],
                "rel_type": row[2], "confidence": row[3], "source_line": row[4],
                "target_name": row[5], "target_id": row[6], "target_name_resolved": row[7],
            })
        return rows

    def close(self) -> None:
        """Close the database connection."""
        del self.conn
        del self.db
