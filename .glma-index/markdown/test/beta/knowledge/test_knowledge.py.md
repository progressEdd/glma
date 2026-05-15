# test/beta/knowledge/test_knowledge.py

8 class(es): TestMemoryKnowledgeStore, TestEventLogWriter, TestDefaultBootstrap, TestAgentBootstrapsOnce, TestDiskKnowledgeStore, TestSqliteKnowledgeStore, _FakeLock, TestLockedKnowledgeStore. 59 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestMemoryKnowledgeStore | class |  |
| TestEventLogWriter | class |  |
| TestDefaultBootstrap | class |  |
| TestAgentBootstrapsOnce | class |  |
| TestDiskKnowledgeStore | class |  |
| TestSqliteKnowledgeStore | class |  |
| _FakeLock | class |  |
| TestLockedKnowledgeStore | class |  |

## Chunks

### TestMemoryKnowledgeStore (class, L32-L100)

> *Summary: This test suite verifies the functionality of a memory-based knowledge store by executing various asynchronous operations. It tests core behaviors such as writing and reading data, listing contents at specific paths, deleting files and directories, checking for existence, and handling path normalization.*


### test_read_write (method, L34-L37, parent: TestMemoryKnowledgeStore)

> *Summary: This asynchronous test verifies the basic read/write functionality of a `MemoryKnowledgeStore`. It writes a string to a specified key and then asserts that reading from that same key returns the exact written value.*


### test_read_nonexistent (method, L40-L42, parent: TestMemoryKnowledgeStore)

> *Summary: This test verifies that attempting to read a non-existent key from an in-memory knowledge store returns `None`. It initializes the store and asserts the expected null return value for the missing path.*


### test_list_root (method, L45-L51, parent: TestMemoryKnowledgeStore)

> *Summary: This test verifies the root listing functionality of a knowledge store by writing two distinct files and asserting that both their paths appear in the returned list from `store.list("/")`. It confirms correct retrieval of top-level directory contents.*


### test_list_subdirectory (method, L54-L59, parent: TestMemoryKnowledgeStore)

> *Summary: This test verifies that listing a directory returns the correct filenames for its contents. It writes two distinct files to a memory store and asserts that `store.list("/log/")` returns an array containing only those file names.*


### test_delete_file (method, L62-L66, parent: TestMemoryKnowledgeStore)

> *Summary: This test verifies file deletion by first writing content to a memory store, then calling the delete method on that file path, and finally asserting that reading the file returns `None`. It confirms the successful removal of data from the knowledge store.*


### test_delete_directory (method, L69-L75, parent: TestMemoryKnowledgeStore)

> *Summary: This test verifies that deleting a directory removes all its contents from the knowledge store. It writes two files into a directory, then deletes the directory, asserting that both original files are subsequently unreadable (return `None`).*


### test_exists (method, L78-L82, parent: TestMemoryKnowledgeStore)

> *Summary: This test verifies the existence checking functionality of a `MemoryKnowledgeStore`. It writes a known key and asserts that `exists()` returns true for it, while also asserting that `exists()` correctly returns false for a non-existent key.*


### test_exists_directory (method, L85-L88, parent: TestMemoryKnowledgeStore)

> *Summary: This asynchronous test verifies that the knowledge store correctly reports the existence of a directory after data has been written to a file within it. It uses an in-memory store to confirm `store.exists()` returns `True` for the parent directory path.*


### test_path_normalization (method, L91-L94, parent: TestMemoryKnowledgeStore)

> *Summary: This test verifies that the knowledge store correctly normalizes paths, allowing a read operation using a leading slash to successfully retrieve data written without one. It uses an in-memory store for this asynchronous check.*


### test_list_empty (method, L97-L100, parent: TestMemoryKnowledgeStore)

> *Summary: This test verifies that listing all knowledge entries from the root path of an in-memory store returns an empty list when no data is present. It initializes a `MemoryKnowledgeStore` and asserts the result of calling its `list("/")` method against an empty array.*


### TestEventLogWriter (class, L103-L198)

> *Summary: These tests verify the `EventLogWriter`'s ability to reliably persist, load, and manage event logs from a knowledge store. It confirms correct sequencing of events across standard persistence, dropped segment handling, concurrent writer isolation, and graceful fallback for unknown event types.*


### test_persist_and_load (method, L105-L126, parent: TestEventLogWriter)

> *Summary: This test verifies the persistence and retrieval mechanism by writing a sequence of model requests and task completions to an in-memory store. It then loads the data back, asserting that the retrieved list contains the correct number of events with matching content for both input and completion records.*


### test_persist_dropped_segments (method, L129-L148, parent: TestEventLogWriter)

> *Summary: This test verifies that segments dropped during compaction are correctly persisted and retrieved in the proper sequence. It simulates writing two sets of dropped requests followed by a final set, then asserts that loading retrieves all three inputs in chronological order.*


### test_persist_dropped_multiple_writers_no_overwrite (method, L151-L177, parent: TestEventLogWriter)

> *Summary: This test verifies that multiple `EventLogWriter` instances writing to the same store do not overwrite each other's data segments. It confirms that three sequential writes from different writers result in a final loaded log containing all three distinct entries.*


### test_load_empty (method, L180-L184, parent: TestEventLogWriter)

> *Summary: This test verifies that loading an empty knowledge store results in an empty list being returned. It initializes a `MemoryKnowledgeStore` and uses an `EventLogWriter` to perform the load operation with a generated UUID.*


### test_unknown_event_fallback (method, L187-L198, parent: TestEventLogWriter)

> *Summary: This test verifies that the event log writer correctly handles unknown event types by falling back to an `UnknownEvent` structure when loading data from a knowledge store. It writes a record with a fake event type and asserts that the loaded result contains exactly one instance of this fallback event.*


### TestDefaultBootstrap (class, L201-L245)

> *Summary: This test suite verifies the behavior of a default bootstrapping mechanism when initializing knowledge stores. It confirms that the bootstrap process correctly creates standard file layouts, respects an existing initialization sentinel to prevent re-running, and crucially, does not write its own initialization sentinel.*


### test_creates_standard_layout (method, L203-L217, parent: TestDefaultBootstrap)

> *Summary: This test verifies that the `DefaultBootstrap` correctly populates a knowledge store after initialization. It asserts the existence of specific keys (like `/SKILL.md`) and confirms that the content of the main skill file contains the expected agent identifier.*


### test_sentinel_prevents_rebootstrap (method, L220-L232, parent: TestDefaultBootstrap)

> *Summary: This test verifies that the presence of an initialization sentinel prevents subsequent bootstrapping operations from running. It first bootstraps with an agent, then overwrites data, and finally asserts the sentinel remains to confirm the skip mechanism works.*


### test_does_not_write_sentinel (method, L235-L245, parent: TestDefaultBootstrap)

> *Summary: This test verifies that the `DefaultBootstrap` process populates a knowledge store with specific files like `/SKILL.md` but intentionally omits writing a sentinel file at `/.initialized`. It achieves this by running the bootstrap against an in-memory store for a given agent name.*


### TestAgentBootstrapsOnce (class, L248-L302)

> *Summary: This test suite verifies that an Agent's knowledge store is bootstrapped only once, even under concurrent requests. It uses a counting mechanism to assert that the `bootstrap` function is called exactly one time when the store is empty, and zero times when a sentinel value already exists in the store.*


### test_concurrent_asks_bootstrap_once (method, L252-L280, parent: TestAgentBootstrapsOnce)

> *Summary: This test verifies that the knowledge bootstrapping process runs only once even when multiple concurrent requests are made to an agent. It uses a custom counter to assert that the `bootstrap` method is called exactly one time during parallel calls to `agent.ask()`.*


### test_existing_sentinel_skips_bootstrap (method, L283-L302, parent: TestAgentBootstrapsOnce)

> *Summary: This test verifies that an existing sentinel value in the knowledge store prevents the bootstrapping process from running when an agent is initialized with a specific configuration. It asserts that the `bootstrap` method on the provided counter object was never called during the agent's execution.*


### TestDiskKnowledgeStore (class, L307-L413)

> *Summary: This test suite verifies the functionality of a disk-backed knowledge store by executing various asynchronous operations against it. It tests core behaviors like reading/writing, persistence across reopens, directory creation, listing contents, deletion (including recursive), and advanced features such as range reads and change event notifications.*


### test_read_write (method, L308-L312, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies the persistence of data by writing a string to a file path within a temporary directory and then reading it back from the store, asserting both the returned value and the actual file content match. It uses an asynchronous disk-based knowledge store for this read/write operation.*


### test_persists_across_reopens (method, L314-L319, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies that data written to a disk knowledge store persists when the store is reinitialized. It writes content to one instance and then reads it back using a newly created instance pointing to the same temporary directory.*


### test_read_nonexistent (method, L321-L323, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies that attempting to read a file path that does not exist from the `DiskKnowledgeStore` returns `None`. It initializes the store using a temporary directory and asserts the expected null return value for the missing key.*


### test_write_creates_parent_directories (method, L325-L329, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies that writing a file to a deep path automatically creates all necessary parent directories within the provided temporary storage location. It confirms both direct file system access and retrieval via the store's read method succeed after the write operation.*


### test_list_root_marks_directories (method, L331-L337, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies the directory listing functionality of a disk-backed knowledge store. It writes two files at different paths and asserts that the root listing returns both the file name and the subdirectory path.*


### test_list_nonexistent_returns_empty (method, L339-L341, parent: TestDiskKnowledgeStore)

> *Summary: When provided with a non-existent path, the knowledge store asynchronously returns an empty list. This test verifies that querying for missing data results in no entries being returned.*


### test_delete_file (method, L343-L348, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies the file deletion functionality of a disk-backed knowledge store. It writes a file, then deletes it via the store's interface, asserting that both the filesystem and the store itself no longer contain the file.*


### test_delete_directory_recursively (method, L350-L356, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies that the `DiskKnowledgeStore` correctly removes a directory and all its contents recursively. It writes files into a structure, then calls delete on the root directory, asserting both filesystem removal and internal state absence.*


### test_delete_missing_is_noop (method, L358-L360, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies that attempting to delete a non-existent file from the disk knowledge store does not raise an error. It initializes the store with a temporary path and calls `delete` on a path known not to exist.*


### test_exists (method, L362-L366, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies the existence checking functionality of a disk-backed knowledge store. It writes a file, asserts that it exists, and then confirms that a non-existent file returns false.*


### test_append_returns_offset (method, L368-L374, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies that the `append` method correctly returns the starting byte offset for each write operation to a disk-backed knowledge store. It confirms that subsequent appends are written sequentially and that the final file content matches the appended data.*


### test_read_range (method, L376-L381, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies the `read_range` functionality of a disk-backed knowledge store by first writing content to a file and then asserting that reading specific byte ranges returns the expected substrings. It confirms correct behavior for both explicit end offsets and omitting the end offset.*


### test_read_range_missing_file (method, L383-L385, parent: TestDiskKnowledgeStore)

> *Summary: When provided with a path to a non-existent file, this test asserts that reading a specified range from the disk knowledge store returns an empty string. It initializes the store using a temporary directory and calls `read_range` on a missing filename.*


### test_path_traversal_blocked (method, L387-L392, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies that the `DiskKnowledgeStore` prevents path traversal attacks when writing data. It asserts that attempting to write to a directory outside the designated root using relative paths raises a `ValueError`.*


### test_on_change_fires_on_write (method, L394-L413, parent: TestDiskKnowledgeStore)

> *Summary: This test verifies that a registered callback fires when data is written to a specific path within the `DiskKnowledgeStore`. It writes content to `/watched/file.txt` and asserts that the provided asynchronous callback receives an event containing "file.txt".*


### TestSqliteKnowledgeStore (class, L417-L544)

> *Summary: This test suite verifies the functionality of a SQLite-backed knowledge store by executing various asynchronous operations against an in-memory or file-based database instance. It tests core features including reading/writing, listing contents, deletion, existence checks, range reads, version tracking, change notifications, and persistence across separate instances.*


### test_read_write (method, L418-L424, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies the read and write functionality of a SQLite knowledge store by first writing content to a specified path and then asserting that reading from the same path returns the exact written value. It ensures proper resource cleanup by closing the store afterward.*


### test_read_nonexistent (method, L426-L431, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies that attempting to read a non-existent file from the knowledge store returns `None`. It initializes an in-memory SQLite store, performs the read operation, and ensures the store is properly closed afterward.*


### test_list_root_and_subdirectory (method, L433-L445, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies the `SqliteKnowledgeStore`'s listing functionality by first writing files at both the root and within a subdirectory. It then asserts that listing the root returns both file names and directory paths, while listing the specific subdirectory only returns its contained files.*


### test_delete_file_and_directory (method, L447-L459, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies the deletion functionality of a knowledge store by first writing files and directories, then calling `delete` on both a file and a directory path. It asserts that after deletion, all corresponding entries are successfully retrieved as `None`.*


### test_exists_file_and_directory (method, L461-L469, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies the `SqliteKnowledgeStore`'s ability to correctly report file and directory existence after writing data. It asserts that a written path exists, a parent directory exists, and a non-existent path returns false.*


### test_append_returns_offset (method, L471-L480, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies that the `append` method correctly returns the starting byte offset for new data and updates the stored content. It uses an in-memory SQLite store to append two lines, asserting the returned offsets match expectations and confirming the final read operation retrieves both appended lines.*


### test_read_range (method, L482-L491, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies the `read_range` functionality of a SQLite knowledge store by writing data and asserting correct substring retrieval for specified start and end indices. It confirms that out-of-bounds or non-existent file reads return an empty string.*


### test_list_versions_under_bumps_per_write (method, L493-L509, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies that listing versions under a given path correctly reflects file changes across writes to an in-memory SQLite knowledge store. It asserts that subsequent calls to list versions show updates for modified files while retaining the state of unchanged files within the specified directory scope.*


### test_on_change_polling (method, L511-L527, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies that a knowledge store correctly triggers a callback when data changes via polling. It initializes the store, subscribes to changes on `/watched`, writes new content to `/watched/file.txt`, and asserts that the registered callback receives the updated path within a timeout.*


### test_close_is_idempotent (method, L529-L532, parent: TestSqliteKnowledgeStore)

> *Summary: Verifies that calling the `close()` method on a knowledge store twice does not result in an error. It initializes a SQLite-backed store and then calls `close()` sequentially to test for idempotency.*


### test_persistence_across_instances (method, L534-L544, parent: TestSqliteKnowledgeStore)

> *Summary: This test verifies that data written to a SQLite knowledge store persists across separate instances. It writes content using one `SqliteKnowledgeStore` instance and then reads the same content back using a newly initialized instance pointing to the same database file.*


### _FakeLock (class, L547-L560)

> *Summary: Provides a minimal mock implementation of a lock mechanism for testing purposes. It tracks which locks are acquired and released by recording names and associated TTLs upon calling `acquire` or `release`.*


### __init__ (method, L550-L553, parent: _FakeLock)

> *Summary: Initializes an object to track knowledge acquisition and release states. It sets up empty lists for storing acquired items with associated scores and released item identifiers, defaulting the acquisition success flag to true.*


### acquire (method, L555-L557, parent: _FakeLock)

> *Summary: This method registers a lock acquisition request by appending the provided name and time-to-live to an internal list. It then returns the current state of the acquisition result.*


### release (method, L559-L560, parent: _FakeLock)

> *Summary: Adds a given string `name` to the internal list of released items. This method modifies the instance's state by appending the provided name to `self.released`.*


### TestLockedKnowledgeStore (class, L564-L682)

> *Summary: This test suite verifies the locking mechanisms of a knowledge store wrapper, ensuring that read operations bypass locks while write, delete, and append operations correctly acquire and release exclusive locks on an underlying memory store. It also confirms proper error handling when lock acquisition fails or when exceptions occur during write/delete operations.*


### test_read_bypasses_lock (method, L565-L572, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that reading from a knowledge store bypasses the locking mechanism when using a fake lock object. It confirms that data written to an inner store is retrievable by the wrapped, locked store without acquiring the provided lock.*


### test_write_acquires_and_releases (method, L574-L583, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that a write operation on a locked knowledge store correctly acquires and releases the underlying lock. It asserts that the specific write action was recorded as acquired and subsequently released by the mock lock, while also confirming the data persistence in the inner store.*


### test_write_raises_when_lock_unavailable (method, L585-L594, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that attempting a write operation on a `LockedKnowledgeStore` fails with a `RuntimeError` if the underlying lock cannot be acquired. It confirms that no data is written to the internal store when the lock acquisition fails.*


### test_write_releases_on_inner_exception (method, L596-L606, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that when an underlying store raises a `ValueError` during a write operation, the system correctly propagates the exception while ensuring the associated lock is released. It uses a mock store to simulate an internal failure and asserts that the expected error occurs and the lock mechanism was properly engaged/released for the specific operation.*


### test_delete_acquires_and_releases (method, L608-L617, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that a locked knowledge store correctly acquires and releases locks during deletion operations. It confirms the lock tracking mechanism records the acquisition of the write lock before deleting the item, and subsequently verifies the data is removed from the underlying store.*


### test_delete_raises_when_lock_unavailable (method, L619-L626, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that attempting a deletion operation on a knowledge store fails with a `RuntimeError` when the underlying lock is unavailable for acquisition. It simulates this failure by setting the fake lock's acquisition result to false before calling the delete method.*


### test_append_acquires_and_returns_offset (method, L628-L645, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that appending data to a locked knowledge store correctly acquires and releases the necessary write locks for each operation. It asserts that the returned offsets match expected values and confirms the lock acquisition/release events recorded by the mock lock object.*


### test_append_raises_when_lock_unavailable (method, L647-L654, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that attempting to append data to a `LockedKnowledgeStore` raises a `RuntimeError` when the underlying lock is unavailable for acquisition. It simulates this failure by setting the fake lock's acquire result to false before calling the append method.*


### test_read_list_exists_read_range_bypass_lock (method, L656-L665, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that read operations on a knowledge store wrapped with a lock function correctly bypass the locking mechanism when reading existing items and ranges. It confirms that listing, existence checks, and range reads return expected values without acquiring the provided lock.*


### test_on_change_bypasses_lock (method, L667-L682, parent: TestLockedKnowledgeStore)

> *Summary: This test verifies that an `on_change` callback fires immediately when data is written to a store wrapped by a lock, even if the underlying write operation occurs while the lock is held. It asserts that the change notification is received and that the lock was not acquired during this specific write sequence.*

