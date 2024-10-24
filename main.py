import lib

def main():
    print("Running Python-Rust Hybrid Tool")
    
    # Call a Python function
    result_python = lib.python_function(5)
    print(f"Python function result: {result_python}")
    
    # Call a Rust function (via PyO3)
    result_rust = lib.rust_function(10)
    print(f"Rust function result: {result_rust}")

if __name__ == "__main__":
    main()