import unittest
from fibonacci import fibonacci, fibonacci_sequence

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        """Test that fibonacci(0) returns 0"""
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_one(self):
        """Test that fibonacci(1) returns 1"""
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        """Test fibonacci for small numbers with known results"""
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)

    def test_fibonacci_larger_number(self):
        """Test fibonacci for a larger number"""
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_negative_input(self):
        """Test that fibonacci raises ValueError for negative input"""
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_sequence_empty(self):
        """Test that fibonacci_sequence(0) returns an empty list"""
        self.assertEqual(fibonacci_sequence(0), [])

    def test_fibonacci_sequence_small(self):
        """Test fibonacci_sequence for a small length"""
        self.assertEqual(fibonacci_sequence(6), [0, 1, 1, 2, 3, 5])

    def test_fibonacci_sequence_negative_length(self):
        """Test that fibonacci_sequence raises ValueError for negative length"""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

if __name__ == '__main__':
    unittest.main()