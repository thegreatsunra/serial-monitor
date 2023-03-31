#!/usr/bin/env python3
"""
Tests
"""

from src.main import hello_world


def test_main():
    """Test main module"""
    assert hello_world() == "Hello World"
