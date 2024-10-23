use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

// A function that prints "Hello, world!" from Rust
#[pyfunction]
fn hello_world() -> PyResult<()> {
    println!("Hello, world! This is from Rust.");
    Ok(())
}

// A function to calculate Fibonacci in Rust and return the result
#[pyfunction]
fn calculate_fibonacci(n: u32) -> PyResult<u32> {
    Ok(fibonacci(n))
}

// An efficient Fibonacci calculation in Rust (iterative approach)
fn fibonacci(n: u32) -> u32 {
    let mut a = 0;
    let mut b = 1;
    for _ in 0..n {
        let temp = a;
        a = b;
        b = temp + b;
    }
    a
}

// Register the Rust functions with Python
#[pymodule]
fn rust_integration(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(hello_world, m)?)?;
    m.add_function(wrap_pyfunction!(calculate_fibonacci, m)?)?;
    Ok(())
}
