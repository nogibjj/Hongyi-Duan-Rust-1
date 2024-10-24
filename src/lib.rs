use pyo3::prelude::*;

/// A simple Rust function to add two numbers
#[pyfunction]
fn rust_function(x: i32) -> i32 {
    x * 2
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_lib(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(rust_function, m)?)?;
    Ok(())
}