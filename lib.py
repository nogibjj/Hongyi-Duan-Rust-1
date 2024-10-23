def hello_world():
    print("Hello, world! This is from Python.")

def calculate_fibonacci(n):
    if n < 0:
        raise ValueError("Negative numbers are not allowed.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def rust_integration():
    from rust_integration import hello_world as rust_hello
    rust_hello()  # Calling Rust's version of `hello_world` for fast computation
