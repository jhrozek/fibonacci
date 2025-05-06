import unittest
from fibonacci import fibonacci, fibonacci_sequence

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_base_cases(self):
        """Test the base cases of fibonacci function (0 and 1)"""
        with self.assertRaises(NotImplementedError):
            fibonacci(0)
        with self.assertRaises(NotImplementedError):
            fibonacci(1)

    def test_fibonacci_positive_number(self):
        """Test fibonacci function with a positive number"""
        with self.assertRaises(NotImplementedError):
            fibonacci(5)

    def test_fibonacci_negative_number(self):
        """Test fibonacci function with a negative number"""
        with self.assertRaises(NotImplementedError):
            fibonacci(-1)

    def test_fibonacci_sequence_empty(self):
        """Test fibonacci_sequence with length 0"""
        self.assertEqual(fibonacci_sequence(0), [])

    def test_fibonacci_sequence_negative_length(self):
        """Test fibonacci_sequence with negative length"""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

    def test_fibonacci_sequence_positive_length(self):
        """Test fibonacci_sequence with positive length"""
        # This will raise NotImplementedError since fibonacci() is not implemented
        with self.assertRaises(NotImplementedError):
            fibonacci_sequence(5)

if __name__ == '__main__':
    unittest.main()