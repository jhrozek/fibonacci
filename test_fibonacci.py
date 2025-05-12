import unittest
from fibonacci import fibonacci, fibonacci_sequence

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_not_implemented(self):
        """Test that fibonacci() raises NotImplementedError"""
        with self.assertRaises(NotImplementedError):
            fibonacci(0)

    def test_fibonacci_sequence_negative_length(self):
        """Test that fibonacci_sequence() raises ValueError for negative length"""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

    def test_fibonacci_sequence_zero_length(self):
        """Test that fibonacci_sequence() returns empty list for length 0"""
        self.assertEqual(fibonacci_sequence(0), [])

    def test_fibonacci_sequence_type(self):
        """Test that fibonacci_sequence() returns a list"""
        result = fibonacci_sequence(0)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
