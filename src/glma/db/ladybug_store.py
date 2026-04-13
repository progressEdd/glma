"""Ladybug graph database store for code chunks and file records."""

from pathlib import Path
from typing import Optional

from real_ladybug import Database, Connection

from glma.models import Chunk, ChunkType, FileRecord, Language, Relationship


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
        file_summary STRING,
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
        data["file_summary"] = data.get("file_summary") or ""
        self.conn.execute(
            """CREATE (f:File {
                path: $path,
                language: $language,
                content_hash: $content_hash,
                last_indexed: $last_indexed,
                chunk_count: $chunk_count,
                file_summary: $file_summary
            })""",
            data,
        )

    def upsert_chunks(self, file_path: str, chunks: list[Chunk]) -> None:
        """Delete existing chunks for a file and insert new ones.

        Preserves existing summaries for chunks whose content_hash hasn't changed.
        This ensures AI-generated summaries survive re-indexing when the code is unchanged.
        """
        # Preserve existing summaries keyed by content_hash
        existing = self.get_chunks_for_file(file_path)
        summary_map = {c.content_hash: c.summary for c in existing if c.summary}

        # Apply preserved summaries to incoming chunks
        for chunk in chunks:
            if not chunk.summary and chunk.content_hash in summary_map:
                chunk.summary = summary_map[chunk.content_hash]

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

    def update_chunk_summary(self, chunk_id: str, summary: str) -> None:
        """Update the summary field of a single chunk.

        Does not delete or recreate the chunk — targeted field update only.

        Args:
            chunk_id: Unique chunk identifier (format: path::type::name::line).
            summary: New summary text to store.
        """
        self.conn.execute(
            "MATCH (c:Chunk {id: $cid}) SET c.summary = $summary",
            {"cid": chunk_id, "summary": summary},
        )

    def update_file_summary(self, file_path: str, summary: str) -> None:
        """Update the file-level LLM summary for a file.

        Args:
            file_path: Relative file path.
            summary: LLM-generated file-level summary.
        """
        self.conn.execute(
            "MATCH (f:File {path: $fp}) SET f.file_summary = $summary",
            {"fp": file_path, "summary": summary},
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

    def get_file_record(self, file_path: str) -> Optional[FileRecord]:
        """Get a file record by path, or None if not indexed."""
        result = self.conn.execute(
            "MATCH (f:File {path: $path}) RETURN f.path, f.language, f.content_hash, f.last_indexed, f.chunk_count, f.file_summary",
            {"path": file_path},
        )
        rows = list(result)
        if not rows:
            return None
        row = rows[0]
        return FileRecord(
            path=row[0],
            language=Language(row[1]),
            content_hash=row[2],
            last_indexed=row[3],
            chunk_count=row[4],
            file_summary=row[5] or None,
        )

    def get_chunks_for_file(self, file_path: str) -> list[Chunk]:
        """Get all chunks for a file, ordered by start_line."""
        result = self.conn.execute(
            """MATCH (c:Chunk {file_path: $fp})
            RETURN c.id, c.name, c.chunk_type, c.file_path, c.content, c.summary,
                   c.start_line, c.end_line, c.content_hash, c.parent_id
            ORDER BY c.start_line""",
            {"fp": file_path},
        )
        chunks = []
        for row in result:
            chunks.append(Chunk(
                id=row[0], name=row[1], chunk_type=ChunkType(row[2]),
                file_path=row[3], content=row[4], summary=row[5] or None,
                start_line=row[6], end_line=row[7], content_hash=row[8],
                parent_id=row[9] or None,
            ))
        return chunks

    def get_all_relationships_for_file(self, file_path: str) -> dict:
        """Get all relationships (outgoing + incoming) for a file's chunks.

        Returns:
            Dict keyed by chunk_id, each value has {"outgoing": [...], "incoming": [...]}.
        """
        relationships: dict[str, dict] = {}

        # Get outgoing relationships
        outgoing = self.get_file_relationships(file_path)
        for rel in outgoing:
            source_id = rel["source_id"]
            if source_id not in relationships:
                relationships[source_id] = {"outgoing": [], "incoming": []}
            # Skip self-referential edges (unresolved targets) for chunks in this file
            if rel["source_id"] == rel["target_id"]:
                # Self-ref edge: still include as outgoing (unresolved target)
                relationships[source_id]["outgoing"].append(rel)
            else:
                relationships[source_id]["outgoing"].append(rel)

        # Get incoming relationships for each chunk
        chunks = self.get_chunks_for_file(file_path)
        chunk_ids = {c.id for c in chunks}
        for chunk in chunks:
            if chunk.id not in relationships:
                relationships[chunk.id] = {"outgoing": [], "incoming": []}
            incoming = self.get_incoming_relationships(chunk.id)
            for rel in incoming:
                source_id = rel["source_id"]
                # Skip self-referential edges where source is also in this file
                if source_id == chunk.id:
                    continue
                # Get source file path
                try:
                    source_result = self.conn.execute(
                        "MATCH (c:Chunk {id: $sid}) RETURN c.file_path",
                        {"sid": source_id},
                    )
                    source_rows = list(source_result)
                    source_file = source_rows[0][0] if source_rows else ""
                except Exception:
                    source_file = ""

                # Skip if source is in the same file (internal refs handled by outgoing)
                if source_file == file_path:
                    continue

                rel["direction"] = "incoming"
                rel["target_id"] = chunk.id
                rel["target_name"] = chunk.name
                rel["target_name_resolved"] = chunk.name
                relationships[chunk.id]["incoming"].append(rel)

        return relationships

    def traverse_relationships(self, chunk_ids: list[str], max_depth: int = 1) -> list[dict]:
        """BFS traversal of relationships up to max_depth hops.

        Args:
            chunk_ids: Starting chunk IDs for traversal.
            max_depth: Maximum traversal depth (1 = direct relationships only).

        Returns:
            List of relationship dicts with added 'depth' field (1-indexed).
        """
        visited = set(chunk_ids)
        queue = [(cid, 1) for cid in chunk_ids]
        results: list[dict] = []

        while queue:
            current_id, depth = queue.pop(0)
            if depth > max_depth:
                continue

            # Get outgoing relationships
            for rel in self.get_outgoing_relationships(current_id):
                target_id = rel.get("target_id", "")
                # Skip self-referential edges
                if current_id == target_id:
                    rel_copy = dict(rel)
                    rel_copy["source_id"] = current_id
                    rel_copy["depth"] = depth
                    results.append(rel_copy)
                    continue
                rel_copy = dict(rel)
                rel_copy["source_id"] = current_id
                rel_copy["depth"] = depth
                results.append(rel_copy)
                if target_id and target_id not in visited:
                    visited.add(target_id)
                    queue.append((target_id, depth + 1))

            # Get incoming relationships
            for rel in self.get_incoming_relationships(current_id):
                source_id = rel.get("source_id", "")
                # Skip self-referential edges
                if current_id == source_id:
                    continue
                rel_copy = dict(rel)
                rel_copy["target_id"] = current_id
                rel_copy["direction"] = "incoming"
                rel_copy["depth"] = depth
                results.append(rel_copy)
                if source_id and source_id not in visited:
                    visited.add(source_id)
                    queue.append((source_id, depth + 1))

        return results

    def close(self) -> None:
        """Close the database connection."""
        del self.conn
        del self.db
