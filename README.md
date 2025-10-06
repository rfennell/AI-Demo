# AI-Demo

A demonstration Python project showcasing best practices and modern Python project structure.

## Features

- ✅ Modern Python package structure with `src` layout
- ✅ Comprehensive unit tests with pytest
- ✅ Type hints and documentation
- ✅ Development tools configuration (black, flake8, pylint, mypy)
- ✅ Proper packaging with pyproject.toml

## Project Structure

```
AI-Demo/
├── src/
│   └── ai_demo/          # Main package
│       ├── __init__.py   # Package initialization
│       └── main.py       # Main module with example functions
├── tests/                # Test directory
│   ├── __init__.py
│   └── test_main.py      # Tests for main module
├── .gitignore            # Git ignore rules
├── pyproject.toml        # Project configuration and metadata
├── requirements.txt      # Production dependencies
├── requirements-dev.txt  # Development dependencies
└── README.md             # This file
```

## Installation

### For Development

1. Clone the repository:
```bash
git clone https://github.com/rfennell/AI-Demo.git
cd AI-Demo
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in editable mode with development dependencies:
```bash
pip install -e .
pip install -r requirements-dev.txt
```

### For Users

```bash
pip install git+https://github.com/rfennell/AI-Demo.git
```

## Usage

### As a Python Module

```python
from ai_demo import greet, calculate

# Use the greet function
message = greet("World")
print(message)  # Output: Hello, World!

# Use the calculate function
result = calculate(5, 3, "add")
print(result)  # Output: 8.0

result = calculate(10, 2, "multiply")
print(result)  # Output: 20.0
```

### As a Command Line Tool

After installation, you can run the demo application:

```bash
ai-demo
```

### Running the Module Directly

```bash
python -m ai_demo.main
```

## Development

### Running Tests

Run all tests with coverage:
```bash
pytest
```

Run tests with verbose output:
```bash
pytest -v
```

Run specific test file:
```bash
pytest tests/test_main.py
```

### Code Formatting

Format code with black:
```bash
black src/ tests/
```

### Linting

Run flake8:
```bash
flake8 src/ tests/
```

Run pylint:
```bash
pylint src/ai_demo
```

### Type Checking

Run mypy:
```bash
mypy src/ai_demo
```

## API Reference

### `greet(name: str) -> str`

Greet a person by name.

**Parameters:**
- `name` (str): The name of the person to greet

**Returns:**
- str: A greeting message

**Raises:**
- `ValueError`: If name is empty

**Example:**
```python
>>> greet("Alice")
'Hello, Alice!'
```

### `calculate(a: float, b: float, operation: str = "add") -> float`

Perform a mathematical operation on two numbers.

**Parameters:**
- `a` (float): First number
- `b` (float): Second number
- `operation` (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

**Returns:**
- float: The result of the operation

**Raises:**
- `ValueError`: If operation is not supported
- `ZeroDivisionError`: If dividing by zero

**Example:**
```python
>>> calculate(5, 3, "add")
8.0
>>> calculate(10, 2, "divide")
5.0
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License.

## Requirements

- Python 3.8 or higher