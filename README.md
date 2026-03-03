# Quick-Calc

Quick-Calc is a simple calculator application developed in Python for the Advanced Software Engineering course. The application supports basic arithmetic operations including addition, subtraction, multiplication, and division. Division by zero is handled safely using controlled exception handling.

This project focuses on clean code structure, proper Git version control practices, and a multi-layered testing strategy including unit and integration testing.

---

## Features

- Addition
- Subtraction
- Multiplication
- Division (with safe zero handling)
- Clear function (resets value to 0)

---

## Project Structure
swe-testing-assignment/
│
├── quick_calc/
│ ├── init.py
│ └── calculator.py
│
├── tests/
│ ├── test_unit_calculator.py
│ └── test_integration_flow.py
│
├── pytest.ini
├── requirements.txt
├── README.md
└── TESTING.md

---

## Setup Instructions

1. Clone the repository:
git clone https://github.com/Oybek2074/swe-testing-assignment.git
cd swe-testing-assignment
2. Create a virtual environment:
py -m venv .venv
.venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

---

## Running the Application

The calculator logic is implemented inside the `Calculator` class located in:
quick_calc/calculator.py

The project focuses on core logic rather than a graphical user interface.

---

## Running Tests

To run all unit and integration tests:
pytest

All tests must pass successfully.

---

## Testing Framework Comparison

Two popular Python testing frameworks were considered for this project: `unittest` and `pytest`.

The `unittest` framework is included in Python’s standard library and follows a class-based structure similar to testing frameworks in other languages. It is reliable and widely used, but it typically requires more boilerplate code, such as defining test classes and setup methods. For small projects, this can make test files longer and slightly harder to read.

On the other hand, `pytest` provides a simpler and more modern approach to testing. It allows writing tests as plain functions, uses clean and readable assertions, and offers powerful built-in features such as exception handling and detailed failure reporting. For this project, where clarity and simplicity were priorities, `pytest` was selected because it reduces boilerplate code, improves readability, and allows faster development of both unit and integration tests.

### unittest
- Built into the Python standard library
- Class-based structure
- More verbose syntax
- Requires additional boilerplate code

### pytest
- Cleaner and more readable syntax
- Powerful assertion introspection
- Built-in support for exception testing
- Minimal boilerplate
- Widely used in modern Python projects

Pytest was selected because it provides better readability, simpler test writing, and more efficient development for small to medium-sized applications.

---

## Version

Release version: **v1.0.0**