class Calculator:
    """
    Quick-Calc core logic.
    Supports: add, subtract, multiply, divide (with safe zero handling), and clear.
    """

    def __init__(self):
        self.clear()

    def clear(self) -> float:
        self.current = 0.0
        return self.current

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        # "Graceful" behavior: raise a clear error instead of crashing randomly.
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b