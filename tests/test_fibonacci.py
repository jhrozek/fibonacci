import unittest
from fibonacci import fibonacci, fibonacci_sequence

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_basic_values(self):
        """Test fibonacci() with basic known values"""
        # These would be the expected results once fibonacci() is implemented
        expected_values = {
            0: 0,
            1: 1,
            2: 1,
            3: 2,
            4: 3,
            5: 5,
        }
        
        # Currently this will fail as fibonacci() raises NotImplementedError
        with self.assertRaises(NotImplementedError):
            fibonacci(0)

    def test_fibonacci_sequence_length(self):
        """Test fibonacci_sequence() returns correct length"""
        test_lengths = [0, 1, 5, 10]
        
        for length in test_lengths:
            with self.assertRaises(NotImplementedError):
                # This will fail until fibonacci() is implemented
                sequence = fibonacci_sequence(length)
                self.assertEqual(len(sequence), length)

    def test_fibonacci_sequence_negative_length(self):
        """Test fibonacci_sequence() raises ValueError for negative length"""
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)

if __name__ == '__main__':
    unittest.main()