import unittest
from fibonacci import fibonacci, fibonacci_sequence

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_base_cases(self):
        """Test the base cases of Fibonacci numbers (0 and 1)"""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_small_numbers(self):
        """Test some known Fibonacci numbers"""
        self.assertEqual(fibonacci(2), 1)  # 0 + 1 = 1
        self.assertEqual(fibonacci(3), 2)  # 1 + 1 = 2
        self.assertEqual(fibonacci(4), 3)  # 1 + 2 = 3
        self.assertEqual(fibonacci(5), 5)  # 2 + 3 = 5

    def test_fibonacci_negative_numbers(self):
        """Test that negative numbers raise ValueError"""
        with self.assertRaises(ValueError):
            fibonacci(-1)

class TestFibonacciSequence(unittest.TestCase):
    def test_empty_sequence(self):
        """Test generating an empty sequence"""
        self.assertEqual(fibonacci_sequence(0), [])

    def test_sequence_length_one(self):
        """Test generating sequence of length 1"""
        self.assertEqual(fibonacci_sequence(1), [0])

    def test_sequence_length_five(self):
        """Test generating sequence of length 5"""
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])

    def test_negative_length(self):
        """Test that negative length raises ValueError"""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

if __name__ == '__main__':
    unittest.main()