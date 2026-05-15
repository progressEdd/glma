# test/test_import_utils.py

5 function(s): mock_module, mock_module_without_version, mock_modules, test_openai_version_higher_than_min, test_openai_version_too_low. 7 class(es): MockModule, TestmoduleInfo, TestOptionalImportBlock, TestRequiresOptionalImportCallables, TestRequiresOptionalImportClasses, TestGetMissingImports, TestVersionAsModule. 19 method(s).

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| mock_module | function |  |
| mock_module_without_version | function |  |
| MockModule | class |  |
| mock_modules | function |  |
| TestmoduleInfo | class |  |
| TestOptionalImportBlock | class |  |
| TestRequiresOptionalImportCallables | class |  |
| TestRequiresOptionalImportClasses | class |  |
| TestGetMissingImports | class |  |
| test_openai_version_higher_than_min | function |  |
| test_openai_version_too_low | function |  |
| TestVersionAsModule | class |  |

## Chunks

### mock_module (function, L21-L27)

> *Summary: Creates and registers a mock `ModuleType` object into `sys.modules`, setting its version to "1.0.0". It yields this created module instance before cleaning up the registration from `sys.modules`.*


### mock_module_without_version (function, L31-L36)

> *Summary: Creates and registers a mock module in `sys.modules` under the name "mock\_module" for testing purposes, yielding the created module instance before cleaning up its registration.*


### MockModule (class, L39-L42)

> *Summary: Represents a mock module object initialized with a string `name` and a string `version`. It stores these two attributes internally for testing purposes.*


### __init__ (method, L40-L42, parent: MockModule)

> *Summary: Initializes an object by storing a provided string `name` and `version` as private attributes. These inputs define the core identity of the instance.*


### mock_modules (function, L46-L59)

> *Summary: This function temporarily injects a predefined set of mock modules into `sys.modules` for testing purposes, yielding the injected modules dictionary before restoring the original system module state upon completion. It ensures that test code interacts with controlled, simulated module objects instead of real ones.*


### TestmoduleInfo (class, L62-L178)

> *Summary: This test suite validates the `ModuleInfo` class by testing its string parsing capabilities against various version specifiers and verifying its logic for checking if a module meets specified version constraints against an installed mock module. It ensures correct behavior when modules are present, absent, or fall outside defined version ranges.*


### test_from_str_success (method, L104-L106, parent: TestmoduleInfo)

> *Summary: This test verifies that the `ModuleInfo.from_str` method correctly parses a string input (`module_info`) into a `ModuleInfo` object, asserting that the resulting object matches the provided expected value.*


### test_from_str_with_invalid_format (method, L108-L111, parent: TestmoduleInfo)

> *Summary: Asserts that attempting to parse a string with an invalid format, like `"jupyter-client>="`, raises a `ValueError` containing the expected error message when using `ModuleInfo.from_str`. This verifies the input validation logic for module information strings.*


### test_is_in_sys_modules (method, L162-L163, parent: TestmoduleInfo)

> *Summary: This test verifies the `is_in_sys_modules` method on a `ModuleInfo` object by asserting its return value matches an expected boolean or string, given mock module and info inputs.*


### test_is_in_sys_modules_without_version (method, L175-L178, parent: TestmoduleInfo)

> *Summary: This test verifies that a `ModuleInfo` object correctly reports whether it resides within the system modules, given a mock module and an expected boolean or string result. It asserts the equality between the method's output and the provided expectation.*


### TestOptionalImportBlock (class, L181-L200)

> *Summary: This test verifies that imports within an `optional_import_block` are scoped locally, ensuring that attempting to use those imported modules outside the block raises an `UnboundLocalError`. It confirms that variables defined only inside the context manager are inaccessible afterward.*


### test_optional_import_block (method, L182-L200, parent: TestOptionalImportBlock)

> *Summary: This test verifies that imports within an `optional_import_block` are scoped locally, allowing the imported modules to be accessed only inside the block. It asserts that attempting to use these modules outside the block raises an `UnboundLocalError`.*


### TestRequiresOptionalImportCallables (class, L203-L371)

> *Summary: This test suite verifies the behavior of a decorator that conditionally requires optional module imports based on specified version constraints or simple presence checks. It tests this mechanism across various callable types, including functions, methods, static methods, and properties, ensuring correct error raising when dependencies are missing or outdated.*


### test_version_too_high (method, L204-L220, parent: TestRequiresOptionalImportCallables)

> *Summary: This test verifies that an `ImportError` is raised when a required module version specified in `@require_optional_import` is not met. It asserts the error message correctly indicates the installed version is too low compared to the requirement.*


### test_function_attributes (method, L223-L247, parent: TestRequiresOptionalImportCallables)

> *Summary: This test verifies that a wrapper function correctly preserves the metadata of an input callable, such as its module and docstring. It asserts that calling the wrapped function either succeeds or raises a specific `ImportError` depending on whether optional dependencies are allowed.*


### test_function_call (method, L250-L266, parent: TestRequiresOptionalImportCallables)

> *Summary: This test verifies the behavior of an optional import mechanism by attempting to call a dummy function under two conditions. If no exceptions are specified, it asserts that calling the function raises an `ImportError` indicating a missing dependency; otherwise, it confirms successful execution when dependencies are available or ignored.*


### test_method_attributes (method, L269-L302, parent: TestRequiresOptionalImportCallables)

> *Summary: This test verifies that a method decorated with `require_optional_import` correctly preserves its metadata (module, name, docstring) while conditionally raising an `ImportError` if the required optional dependency is missing when no exceptions are allowed. It uses a dummy class to simulate modifying module attributes before applying the decorator.*


### test_method_call (method, L305-L324, parent: TestRequiresOptionalImportCallables)

> *Summary: This test verifies the behavior of a method decorator that conditionally requires an optional module import. It asserts that calling the decorated method raises an `ImportError` if no exception handling is specified, but allows execution if exceptions are permitted.*


### test_static_call (method, L327-L347, parent: TestRequiresOptionalImportCallables)

> *Summary: This test verifies the behavior of a static method decorated with `@require_optional_import`. It asserts that calling the method raises an `ImportError` if no exceptions are specified, simulating a missing optional dependency, while successfully executing when exceptions are provided.*


### test_property_call (method, L350-L371, parent: TestRequiresOptionalImportCallables)

> *Summary: This test verifies that a property decorated with `require_optional_import` raises an `ImportError` if the specified optional dependency is missing, unless explicitly told not to raise the error via the `except_for` argument. When dependencies are present or when testing the success path, it executes the property call without raising an exception.*


### TestRequiresOptionalImportClasses (class, L374-L407)

> *Summary: This test fixture creates a class decorated to require an optional dependency, and the associated test verifies that instantiating this class raises an `ImportError` if the specified module is not installed. It specifically checks for a detailed error message indicating the missing optional dependency.*


### dummy_cls (method, L376-L398, parent: TestRequiresOptionalImportClasses)

> *Summary: This method dynamically creates and returns a `DummyClass` containing various methods (instance, static, class), properties, and a placeholder method. It uses `@require_optional_import` to conditionally load dependencies for testing purposes.*


### test_class_init_call (method, L400-L407, parent: TestRequiresOptionalImportClasses)

> *Summary: Asserts that instantiating a class will raise an `ImportError` if a required optional dependency, specifically `'some_optional_module'`, is missing. This test verifies the error message format when initialization fails due to a missing package.*


### TestGetMissingImports (class, L410-L456)

> *Summary: This test suite verifies the `get_missing_imports` function by providing various lists of required module specifications as input. It asserts that the returned dictionary accurately reflects which modules are either missing or installed at an incorrect version according to the specified constraints.*


### test_get_missing_imports (method, L451-L456, parent: TestGetMissingImports)

> *Summary: This test verifies the `get_missing_imports` function by providing a set of available modules and a list of required module names. It asserts that the returned dictionary of missing imports exactly matches the predefined expected result.*


### test_openai_version_higher_than_min (function, L459-L470)

> *Summary: This test simulates an `openai` module with a high version number and checks if its requirement (`>=1.66.2`) is met by calling `is_in_sys_modules()`. It asserts that the method returns `None`, indicating the installed version satisfies the minimum requirement.*


### test_openai_version_too_low (function, L473-L483)

> *Summary: This test simulates an outdated `openai` module by patching `sys.modules` to report a version of "1.0.0". It then asserts that checking the required minimum version ("openai>=1.66.2") correctly identifies the installed version as too low.*


### TestVersionAsModule (class, L486-L568)

> *Summary: This test suite verifies how a system handles package versions when the `__version__` attribute points to an imported module instead of a string. It uses fixtures to dynamically create mock packages with module-based versions and tests two scenarios: one where version constraints are present, expecting a specific error message, and another without constraints, expecting no result.*


### mock_package_with_module_version (method, L492-L533, parent: TestVersionAsModule)

> *Summary: Sets up a mock package structure where the `__version__` attribute is itself a module object by creating necessary files and manipulating `sys.path`. It yields control after setting up the environment, allowing tests to import this specific package configuration before cleaning up all created directories and path entries upon completion.*


### test_handle_module_as_version_with_constraints (method, L535-L551, parent: TestVersionAsModule)

> *Summary: This test verifies how the system handles a module specified with a version constraint. It takes a string like `"module>=1.0"` to create a `ModuleInfo` and asserts that calling `is_in_sys_modules()` returns a specific error message instead of crashing.*


### test_handle_module_as_version_no_constraints (method, L553-L568, parent: TestVersionAsModule)

> *Summary: When a `ModuleInfo` object is created without any specified version constraints, calling `is_in_sys_modules()` returns `None`, even if the underlying package's version attribute is not a string. This confirms that the absence of constraints bypasses strict type checking for module versions.*

