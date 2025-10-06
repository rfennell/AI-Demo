"""Tests for the main module."""

import pytest
from ai_demo.main import greet, calculate


class TestGreet:
    """Tests for the greet function."""
    
    def test_greet_with_name(self):
        """Test greeting with a valid name."""
        result = greet("Alice")
        assert result == "Hello, Alice!"
    
    def test_greet_with_different_name(self):
        """Test greeting with a different name."""
        result = greet("Bob")
        assert result == "Hello, Bob!"
    
    def test_greet_with_empty_string(self):
        """Test greeting with an empty string raises ValueError."""
        with pytest.raises(ValueError, match="Name cannot be empty"):
            greet("")


class TestCalculate:
    """Tests for the calculate function."""
    
    def test_addition(self):
        """Test addition operation."""
        result = calculate(5, 3, "add")
        assert result == 8.0
    
    def test_subtraction(self):
        """Test subtraction operation."""
        result = calculate(10, 4, "subtract")
        assert result == 6.0
    
    def test_multiplication(self):
        """Test multiplication operation."""
        result = calculate(6, 7, "multiply")
        assert result == 42.0
    
    def test_division(self):
        """Test division operation."""
        result = calculate(20, 4, "divide")
        assert result == 5.0
    
    def test_division_by_zero(self):
        """Test division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            calculate(10, 0, "divide")
    
    def test_unsupported_operation(self):
        """Test unsupported operation raises ValueError."""
        with pytest.raises(ValueError, match="Unsupported operation"):
            calculate(5, 3, "modulo")
    
    def test_default_operation(self):
        """Test default operation is addition."""
        result = calculate(2, 3)
        assert result == 5.0
