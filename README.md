# Hongyi-Duan-Rust-1

[![Python CI/CD Pipeline](https://github.com/nogibjj/Hongyi-Duan-Rust-1/actions/workflows/PythonCI.yml/badge.svg)](https://github.com/nogibjj/Hongyi-Duan-Rust-1/actions/workflows/PythonCI.yml)

This project demonstrates the integration of Python and Rust, focusing on packaging a Python script into a Rust-based package. The repository includes several components like continuous integration (CI) pipelines, test scripts, and documentation that support seamless development and deployment across both programming environments.

## Project Overview

This project packages a Python script (`main.py`) into a Rust-based module. It showcases a hybrid development approach that leverages the advantages of Rust's performance and Python's flexibility. The repository also contains tools for testing, CI/CD pipelines, and comprehensive documentation.

### Key Features:
- **Hybrid Python-Rust Module**: A Python script converted into a Rust package.
- **Continuous Integration**: Implemented CI/CD pipelines for automated testing and deployment using GitHub Actions.
- **Modular Design**: Each script is clearly divided to handle extraction, transformation, querying, and testing.
- **Documentation**: Detailed explanations and user guides for understanding and using the module.
  
## Directory Structure

```bash
Hongyi-Duan-Rust-1/
│
├── .github/                    # GitHub Actions workflows for CI/CD pipelines
│   ├── pythonCI.yml             # Python CI pipeline
│   └── rustCI.yml               # Rust CI pipeline
│
├── src/                        # Rust source code
│   └── lib.rs                  # Main Rust library file
│
├── tests/                      # Test files
│   └── test_main.py            # Unit tests for Python
│
├── Cargo.toml                  # Rust package configuration file
├── main.py                     # Main Python script to be packaged into Rust
├── test_main.py                # Python test script
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
├── LICENSE                     # License for the project
└── .gitignore                  # Files and directories to be ignored by Git
```

## Requirements

To get started with this project, ensure you have the following dependencies installed:

- **Python**: Version 3.x
- **Rust**: Stable version installed with `cargo`
- **Git**: To clone the repository and manage version control
- Python libraries listed in `requirements.txt`

### Setting Up Python and Rust

1. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Install Rust and `cargo` if not already installed:
    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```

## Usage

### Running the Python Script

To run the Python script (`main.py`) independently, use the following command:

```bash
python main.py
```

### Running Tests

Tests for the Python code are located in `test_main.py`. Run the tests using:

```bash
python -m unittest test_main.py
```

### Packaging Python into Rust

The main goal of this project is to package the Python script into a Rust module. To achieve this, the Rust source file (`lib.rs`) is used to interface with Python using the [PyO3](https://github.com/PyO3/pyo3) library.

1. Compile the Rust code:
    ```bash
    cargo build --release
    ```

2. Link the compiled Rust package to your Python environment using the `maturin` tool, which allows packaging Rust as a Python module.

```bash
pip install maturin
maturin develop
```

3. Now you can use the Rust-based module directly in Python.

## CI/CD Pipelines

This repository uses GitHub Actions to automate testing and deployment. There are two primary CI pipelines configured:

- **Python CI** (`pythonCI.yml`): Runs Python tests automatically upon each commit.
- **Rust CI** (`rustCI.yml`): Runs Rust build and test workflows to ensure that the code remains functional across all updates.

Both workflows are triggered on every push and pull request to the repository.

### Python CI Pipeline

This workflow runs unit tests for Python code using `unittest` framework and checks for any issues or failures in the scripts.

### Rust CI Pipeline

This workflow compiles the Rust code and runs tests to validate the functionality of the Rust module.
