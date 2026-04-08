"""Helper for creating test project structures."""

from pathlib import Path


def create_test_project(tmp_path: Path) -> Path:
    """Create a realistic multi-file project for integration testing.

    Creates:
        test_project/
        ├── .git/HEAD
        ├── venv/lib.py
        ├── node_modules/package.js
        ├── src/main.c
        ├── src/utils.h
        ├── src/app.py
        ├── src/helpers.py
        ├── README.md
        └── .hidden.py

    Returns:
        Path to the test project root.
    """
    root = tmp_path / "test_project"

    # Create directories
    (root / ".git").mkdir(parents=True)
    (root / "venv").mkdir(parents=True)
    (root / "node_modules").mkdir(parents=True)
    (root / "src").mkdir(parents=True)

    # Files that should be skipped
    (root / ".git" / "HEAD").write_text("ref: refs/heads/main\n")
    (root / "venv" / "lib.py").write_text("# venv file\ndef venv_func(): pass\n")
    (root / "node_modules" / "package.js").write_text("module.exports = {};\n")
    (root / "README.md").write_text("# Test Project\n")
    (root / ".hidden.py").write_text("def hidden(): pass\n")

    # C source files
    (root / "src" / "main.c").write_text("""\
#include <stdio.h>
#include "utils.h"

/* Main entry point */
int main(int argc, char **argv) {
    struct Point p = make_point(1, 2);
    printf("Point: %d, %d\\n", p.x, p.y);
    return 0;
}
""")

    (root / "src" / "utils.h").write_text("""\
#ifndef UTILS_H
#define UTILS_H

struct Point {
    int x;
    int y;
};

struct Point make_point(int x, int y);

#endif
""")

    # Python source files
    (root / "src" / "app.py").write_text('''\
"""Application module with a user class."""

import os
from typing import Optional


class User:
    """Represents a user in the system."""

    def __init__(self, name: str, email: str):
        """Initialize user with name and email."""
        self.name = name
        self.email = email

    def greet(self) -> str:
        """Return a greeting for this user."""
        return f"Hello, {self.name}!"

    def to_dict(self) -> dict:
        """Convert user to dictionary."""
        return {"name": self.name, "email": self.email}


def create_user(name: str, email: str = None) -> Optional[User]:
    """Factory function to create a user."""
    if not name:
        return None
    return User(name, email or "")
''')

    (root / "src" / "helpers.py").write_text('''\
# Helper utilities for the project

import json


def load_config(path: str) -> dict:
    """Load a JSON config file."""
    with open(path) as f:
        return json.load(f)


# Format a message with given parameters

def format_message(template: str, **kwargs) -> str:
    """Format a message template with kwargs."""
    return template.format(**kwargs)
''')

    return root
