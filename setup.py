from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name='simplecalc',
    version='0.1',
    packages=[''],
    rust_extensions=[RustExtension('rust_ext.rust_ext', 'rust_ext/Cargo.toml', binding=Binding.PyO3)],
    scripts=['main.py'],
    entry_points={
        'console_scripts': [
            'simplecalc = main:main'
        ],
    },
    install_requires=['setuptools-rust'],
    setup_requires=['setuptools-rust>=1.1.0'],
    author='Hongyi Duan',
    author_email='hd162@duke.edu',
    description='A simple calculator tool with Rust acceleration',
    keywords='calculator math rust',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Rust',
    ],
    zip_safe=False,
)
