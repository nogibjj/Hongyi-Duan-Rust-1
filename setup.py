from setuptools import setup
from setuptools_rust import RustExtension

setup(
    name="rust_python_integration",
    version="0.1.0",
    packages=["src"],
    rust_extensions=[RustExtension("rust_integration.rust_integration", "Cargo.toml")],
    zip_safe=False,
)
