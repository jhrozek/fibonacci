import unittest
import sys
import os
from pathlib import Path

# Add parent directory to path so we can import the fibonacci module
sys.path.append(str(Path(__file__).parent.parent))

from fibonacci import fibonacci, fibonacci_sequence


class TestFibonacci(unittest.TestCase):
    """Test cases for the fibonacci function"""

    def test_fibonacci_zero(self):
        """Test fibonacci(0) returns 0"""
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        """Test fibonacci(1) returns 1"""
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_values(self):
        """Test fibonacci function with small values"""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)

    def test_fibonacci_larger_value(self):
        """Test fibonacci function with a larger value"""
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_negative_input(self):
        """Test fibonacci function raises ValueError for negative input"""
        with self.assertRaises(ValueError) as context:
            fibonacci(-1)
        self.assertIn("Input must be a non-negative integer", str(context.exception))


class TestFibonacciSequence(unittest.TestCase):
    """Test cases for the fibonacci_sequence function"""

    def test_empty_sequence(self):
        """Test fibonacci_sequence(0) returns an empty list"""
        self.assertEqual(fibonacci_sequence(0), [])

    def test_sequence_length_one(self):
        """Test fibonacci_sequence(1) returns [0]"""
        self.assertEqual(fibonacci_sequence(1), [0])

    def test_sequence_length_two(self):
        """Test fibonacci_sequence(2) returns [0, 1]"""
        self.assertEqual(fibonacci_sequence(2), [0, 1])

    def test_sequence_length_ten(self):
        """Test fibonacci_sequence(10) returns first 10 Fibonacci numbers"""
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fibonacci_sequence(10), expected)

    def test_negative_length(self):
        """Test fibonacci_sequence raises ValueError for negative length"""
        with self.assertRaises(ValueError) as context:
            fibonacci_sequence(-1)
        self.assertIn("Length must be a non-negative integer", str(context.exception))


if __name__ == "__main__":
    unittest.main()