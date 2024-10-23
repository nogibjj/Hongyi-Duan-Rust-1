from lib import hello_world, calculate_fibonacci, rust_integration

def main():
    print("Welcome to the Python-Rust Integration tool!")

    # Call Python-based function
    hello_world()

    # Example: Calculate Fibonacci
    try:
        n = int(input("Enter a number to calculate Fibonacci: "))
        print(f"Fibonacci of {n} is: {calculate_fibonacci(n)}")
    except ValueError as e:
        print(f"Invalid input: {e}")

    # Example: Call a Rust function for fast computation
    print("Now calling Rust for performance-critical tasks...")
    rust_integration()
    
    print("Program completed successfully.")

if __name__ == "__main__":
    main()

