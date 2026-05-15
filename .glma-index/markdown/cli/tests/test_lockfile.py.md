# cli/tests/test_lockfile.py

1 class(es): TestLockfile. 8 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| TestLockfile | class |  |

## Chunks

### TestLockfile (class, L6-L98)

> *Summary: These tests verify the functionality of a `Lockfile` class, which manages installation records by reading and writing to a file path provided as input. It allows recording installations with specific references, versions, targets, and files, checking for existing installs, handling uninstalls, listing all recorded items, and ensuring data persists across operations.*


### test_empty_lockfile (method, L9-L14, parent: TestLockfile)

> *Summary: Verifies that an initialized `Lockfile` object, when pointed to an empty directory, correctly reports no installed packages and that a specific package is not found. It confirms the initial state of the lockfile management system.*


### test_record_and_check_install (method, L16-L30, parent: TestLockfile)

> *Summary: This test verifies the functionality of a `Lockfile` by first recording an installation record for a specific package and version, then asserting that the file correctly reports the presence of that exact installation while denying checks for different versions or non-existent packages. It uses a temporary directory as input to manage the lockfile state.*


### test_lockfile_persists_to_disk (method, L32-L43, parent: TestLockfile)

> *Summary: Verifies that installation records persist across process restarts by creating a `Lockfile` instance, recording an install, and then loading a new instance from the same temporary directory to confirm the data integrity. It asserts that the recorded package is present and has the correct version upon reloading.*


### test_record_uninstall (method, L45-L54, parent: TestLockfile)

> *Summary: This test verifies the uninstall functionality of a `Lockfile` object by first recording an installation and then calling `record_uninstall`. It asserts that the uninstallation process returns valid information and correctly marks the package as no longer installed.*


### test_uninstall_nonexistent_returns_none (method, L56-L60, parent: TestLockfile)

> *Summary: Verifies that attempting to record the uninstallation of a non-existent skill returns `None`. It initializes a `Lockfile` object within a temporary directory and calls its `record_uninstall` method with an invalid path.*


### test_list_installed (method, L62-L72, parent: TestLockfile)

> *Summary: This test verifies the `Lockfile`'s ability to track installations by first recording two distinct package entries and then asserting that the returned list contains exactly those two recorded references. It confirms correct retrieval of installed items from the lockfile object.*


### test_overwrite_existing_install (method, L74-L83, parent: TestLockfile)

> *Summary: This test verifies that recording a newer installation overwrites older versions for the same reference. It confirms that only the latest recorded version remains listed after multiple calls to `record_install`.*


### test_files_stored_as_relative (method, L85-L98, parent: TestLockfile)

> *Summary: This test verifies that file paths recorded in a `Lockfile` are stored relative to the lockfile's location. It records an installation with absolute file paths and asserts that retrieving the installation returns those files as relative paths.*

