import unittest
from fibonacci import fibonacci, fibonacci_sequence

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        """Test fibonacci(0) returns 0"""
        self.assertEqual(fibonacci(0), 0)
    
    def test_fibonacci_one(self):
        """Test fibonacci(1) returns 1"""
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_basic(self):
        """Test some basic fibonacci numbers"""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
    
    def test_fibonacci_negative(self):
        """Test fibonacci with negative input raises ValueError"""
        with self.assertRaises(ValueError):
            fibonacci(-1)
    
    def test_fibonacci_sequence_empty(self):
        """Test empty fibonacci sequence"""
        self.assertEqual(fibonacci_sequence(0), [])
    
    def test_fibonacci_sequence_basic(self):
        """Test basic fibonacci sequence"""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci_sequence(10), expected)
    
    def test_fibonacci_sequence_negative_length(self):
        """Test fibonacci sequence with negative length raises ValueError"""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

if __name__ == '__main__':
    unittest.main()