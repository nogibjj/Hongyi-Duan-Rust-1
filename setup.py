from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="python-rust-hybrid",
    version="0.1.0",
    packages=["lib"],
    rust_extensions=[RustExtension("rust_lib", "Cargo.toml", binding="pyo3")],
    zip_safe=False,
)