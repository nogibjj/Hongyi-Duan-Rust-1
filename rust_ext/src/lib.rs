use pyo3::prelude::*;

#[pyfunction]
fn add(a: f64, b: f64) -> PyResult<f64> {
    Ok(a + b)
}

#[pyfunction]
fn subtract(a: f64, b: f64) -> PyResult<f64> {
    Ok(a - b)
}

#[pyfunction]
fn multiply(a: f64, b: f64) -> PyResult<f64> {
    Ok(a * b)
}

#[pyfunction]
fn divide(a: f64, b: f64) -> PyResult<f64> {
    if b == 0.0 {
        Err(PyErr::new::<pyo3::exceptions::PyValueError, _>("Cannot divide by zero."))
    } else {
        Ok(a / b)
    }
}

#[pymodule]
fn rust_ext(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add, m)?)?;
    m.add_function(wrap_pyfunction!(subtract, m)?)?;
    m.add_function(wrap_pyfunction!(multiply, m)?)?;
    m.add_function(wrap_pyfunction!(divide, m)?)?;
    Ok(())
}
