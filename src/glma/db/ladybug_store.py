"""Ladybug graph database store for code chunks and file records."""

from pathlib import Path
from typing import Optional

from real_ladybug import Database, Connection

from glma.models import Chunk, FileRecord


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

    def close(self) -> None:
        """Close the database connection."""
        del self.conn
        del self.db
