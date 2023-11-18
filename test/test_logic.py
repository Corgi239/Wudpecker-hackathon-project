"""
Test the logic module

Files in folder test are automatically run by pytest
Naming convention is test_<name of module to test>.py
"""
from src.logic import example_func


def test_example_func():
    """Test example_func"""
    assert example_func().shape == (1, 5)
