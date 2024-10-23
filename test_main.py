import unittest
from lib import hello_world, calculate_fibonacci, rust_integration

class TestMain(unittest.TestCase):
    
    def test_hello_world(self):
        # Capture the output of the hello_world function
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        hello_world()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello, world! This is from Python.\n")

    def test_calculate_fibonacci(self):
        # Test Fibonacci calculation
        self.assertEqual(calculate_fibonacci(0), 0)
        self.assertEqual(calculate_fibonacci(1), 1)
        self.assertEqual(calculate_fibonacci(5), 5)
        self.assertEqual(calculate_fibonacci(10), 55)
        
        # Test for invalid input
        with self.assertRaises(ValueError):
            calculate_fibonacci(-1)
        
    def test_rust_integration(self):
        # Test Rust function interaction
        # Capture the output of the Rust function
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        rust_integration()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "Hello, world! This is from Rust.\n")

if __name__ == "__main__":
    unittest.main()
