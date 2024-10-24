import rust_lib

def python_function(x):
    """Python function to return square of a number."""
    return x * x

def rust_function(x):
    """Rust function imported from Rust using PyO3."""
    return rust_lib.rust_function(x)