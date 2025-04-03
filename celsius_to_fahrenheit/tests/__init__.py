import pytest
import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    print("test test")
    result = celsius_to_fahrenheit(100)
    assert result == 212
