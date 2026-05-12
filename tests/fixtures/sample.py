"""A sample Python file for testing."""

import os
from pathlib import Path


def standalone_function(x: int) -> int:
    """A standalone function."""
    return x * 2


class MyClass:
    """A sample class."""

    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f"Hello, {self.name}"


def another_function():
    pass
