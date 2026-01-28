"""Minimal demo module for CI and unit testing."""

from __future__ import annotations


def greet(name: str) -> str:
    """Return a friendly greeting for a user-provided name."""
    clean = name.strip()
    if not clean:
        raise ValueError("name must be non-empty")
    return f"Hello, {clean}!"


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def is_even(value: int) -> bool:
    """Return True when the number is even."""
    return value % 2 == 0
