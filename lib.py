try:
    from rust_ext import add, subtract, multiply, divide
except ImportError:
    # Fallback to pure Python implementation if Rust module not available
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
