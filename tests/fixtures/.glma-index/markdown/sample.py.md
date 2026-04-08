# sample.py

*(File summary not yet generated — available after Phase 3.)*

## Key Exports

| Name | Type | Description |
| ---- | ---- | ----------- |
| standalone_function | function | A standalone function. |
| MyClass | class | A sample class. |
| another_function | function |  |

## Chunks

### standalone_function (function, L7-L9)

A standalone function.

```python
def standalone_function(x: int) -> int:
    """A standalone function."""
    return x * 2
```

### MyClass (class, L12-L19)

A sample class.

```python
class MyClass:
    """A sample class."""

    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}"
```

### __init__ (method, L15-L16, parent: MyClass)

```python
def __init__(self, name: str):
        self.name = name
```

### greet (method, L18-L19, parent: MyClass)

```python
def greet(self) -> str:
        return f"Hello, {self.name}"
```

### another_function (function, L22-L23)

```python
def another_function():
    pass
```
