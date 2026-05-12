---
wave: 1
depends_on: []
files_modified:
  - src/glma/db/ladybug_store.py
  - src/glma/models.py
requirements_addressed:
  - PIPE-02
---

# Plan 02: Pipeline Stage Tracking (PIPE-02)

## Objective
Add `pipeline_stage` property to File nodes in LadybugStore, with 4 stages: `discovered`, `chunked`, `relationships_extracted`, `complete`. Add store methods to query and update stages. Update FileRecord model.

## Tasks

### Task 2.1: Add `pipeline_stage` to FileRecord model

<read_first>
- 02-worktrees/glma/src/glma/models.py — `FileRecord` class (around line 46)
</read_first>

<action>
Add `pipeline_stage` field to `FileRecord`:
```python
class FileRecord(BaseModel):
    """Record of an indexed file."""
    path: str = Field(..., description="Relative path from repo root")
    language: Language
    content_hash: str = Field(..., description="BLAKE2b hash of file content")
    last_indexed: str = Field(..., description="ISO 8601 timestamp")
    chunk_count: int = Field(default=0)
    file_summary: Optional[str] = Field(default=None, description="LLM-generated file-level summary")
    pipeline_stage: str = Field(default="discovered", description="Pipeline stage: discovered, chunked, relationships_extracted, complete")
```
</action>

<acceptance_criteria>
- `models.py` `FileRecord` class contains `pipeline_stage: str = Field(default="discovered", ...)`
- Creating a `FileRecord` without specifying `pipeline_stage` defaults to `"discovered"`
</acceptance_criteria>

---

### Task 2.2: Add `pipeline_stage` to SCHEMA_FILES and upsert_file

<read_first>
- 02-worktrees/glma/src/glma/db/ladybug_store.py — `SCHEMA_FILES` string (around line 30), `upsert_file()` method (around line 140), `_migrate_schema()` method (around line 175)
</read_first>

<action>
1. Add `pipeline_stage STRING` to `SCHEMA_FILES`:
   ```python
   SCHEMA_FILES = """
   CREATE NODE TABLE IF NOT EXISTS File (
       path STRING,
       language STRING,
       content_hash STRING,
       last_indexed STRING,
       chunk_count INT64,
       file_summary STRING,
       pipeline_stage STRING,
       PRIMARY KEY (path)
   )
   """
   ```

2. Update `upsert_file()` to include `pipeline_stage` in the CREATE statement:
   ```python
   data["pipeline_stage"] = data.get("pipeline_stage", "discovered")
   self.conn.execute(
       """CREATE (f:File {
           path: $path,
           language: $language,
           content_hash: $content_hash,
           last_indexed: $last_indexed,
           chunk_count: $chunk_count,
           file_summary: $file_summary,
           pipeline_stage: $pipeline_stage
       })""",
       data,
   )
   ```

3. Add migration in `_migrate_schema()`:
   ```python
   migrations = [
       f"ALTER TABLE Chunk ADD embedding FLOAT[{self._vector_dims}]",
       "ALTER TABLE Chunk ADD summary_hash STRING",
       "ALTER TABLE Chunk ADD vector_dimensions INT64",
       "ALTER TABLE File ADD pipeline_stage STRING",
   ]
   ```

4. Add `set_pipeline_stage()` method:
   ```python
   def set_pipeline_stage(self, file_path: str, stage: str) -> None:
       """Update the pipeline_stage property of a file node.
       
       Args:
           file_path: Relative file path.
           stage: Pipeline stage (discovered, chunked, relationships_extracted, complete).
       """
       self.conn.execute(
           "MATCH (f:File {path: $fp}) SET f.pipeline_stage = $stage",
           {"fp": file_path, "stage": stage},
       )
   ```

5. Add `get_incomplete_files()` method:
   ```python
   def get_incomplete_files(self) -> list[tuple[str, str]]:
       """Get files that haven't completed the pipeline.
       
       Returns:
           List of (file_path, pipeline_stage) tuples for files where stage != 'complete',
           ordered by file path.
       """
       result = self.conn.execute(
           """MATCH (f:File)
           WHERE f.pipeline_stage IS NULL OR f.pipeline_stage <> 'complete'
           RETURN f.path, f.pipeline_stage
           ORDER BY f.path"""
       )
       return [(row[0], row[1] or "discovered") for row in result]
   ```
</action>

<acceptance_criteria>
- `ladybug_store.py` `SCHEMA_FILES` contains `pipeline_stage STRING`
- `ladybug_store.py` `upsert_file()` includes `pipeline_stage` in the CREATE Cypher
- `ladybug_store.py` `_migrate_schema()` includes migration line `ALTER TABLE File ADD pipeline_stage STRING`
- `ladybug_store.py` has method `def set_pipeline_stage(self, file_path: str, stage: str) -> None:`
- `ladybug_store.py` has method `def get_incomplete_files(self) -> list[tuple[str, str]]:`
- `models.py` `FileRecord` has `pipeline_stage` field with default `"discovered"`
- Existing tests pass (schema migration is backward-compatible — new column added via ALTER)
</acceptance_criteria>

---
