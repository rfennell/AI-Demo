"""Main module for AI Demo application."""


def greet(name: str) -> str:
    """Greet a person by name.
    
    Args:
        name: The name of the person to greet
        
    Returns:
        A greeting message
        
    Example:
        >>> greet("Alice")
        'Hello, Alice!'
    """
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"


def calculate(a: float, b: float, operation: str = "add") -> float:
    """Perform a mathematical operation on two numbers.
    
    Args:
        a: First number
        b: Second number
        operation: The operation to perform ('add', 'subtract', 'multiply', 'divide')
        
    Returns:
        The result of the operation
        
    Raises:
        ValueError: If operation is not supported
        ZeroDivisionError: If dividing by zero
        
    Example:
        >>> calculate(5, 3, "add")
        8.0
        >>> calculate(10, 2, "divide")
        5.0
    """
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y,
    }
    
    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}. Choose from {list(operations.keys())}")
    
    return float(operations[operation](a, b))


def main() -> None:
    """Main entry point for the application."""
    print("Welcome to AI Demo!")
    print(greet("World"))
    print(f"5 + 3 = {calculate(5, 3, 'add')}")
    print(f"10 * 2 = {calculate(10, 2, 'multiply')}")


if __name__ == "__main__":
    main()
