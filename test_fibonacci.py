import unittest
from fibonacci import fibonacci, fibonacci_sequence

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        """Test fibonacci(0) returns 0"""
        self.assertEqual(fibonacci(0), 0)
    
    def test_fibonacci_one(self):
        """Test fibonacci(1) returns 1"""
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_two(self):
        """Test fibonacci(2) returns 1"""
        self.assertEqual(fibonacci(2), 1)
    
    def test_fibonacci_small_number(self):
        """Test fibonacci(5) returns correct value"""
        self.assertEqual(fibonacci(5), 5)  # 0,1,1,2,3,5
    
    def test_fibonacci_negative(self):
        """Test fibonacci() with negative input raises ValueError"""
        with self.assertRaises(ValueError):
            fibonacci(-1)

class TestFibonacciSequence(unittest.TestCase):
    def test_empty_sequence(self):
        """Test fibonacci_sequence(0) returns empty list"""
        self.assertEqual(fibonacci_sequence(0), [])
    
    def test_sequence_length_one(self):
        """Test fibonacci_sequence(1) returns [0]"""
        self.assertEqual(fibonacci_sequence(1), [0])
    
    def test_sequence_length_five(self):
        """Test fibonacci_sequence(5) returns correct sequence"""
        self.assertEqual(fibonacci_sequence(5), [0, 1, 1, 2, 3])
    
    def test_negative_length(self):
        """Test fibonacci_sequence() with negative length raises ValueError"""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

if __name__ == '__main__':
    unittest.main()
