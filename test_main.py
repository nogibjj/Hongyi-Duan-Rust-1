import unittest
import lib

class TestHybridTool(unittest.TestCase):
    
    def test_python_function(self):
        self.assertEqual(lib.python_function(5), 25)
    
    def test_rust_function(self):
        self.assertEqual(lib.rust_function(10), 20)

if __name__ == '__main__':
    unittest.main()