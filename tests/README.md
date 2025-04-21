# Fibonacci Tests

This directory contains tests for the Fibonacci implementation.

## Running the Tests

You can run the tests using the following command from the root directory:

```bash
python -m unittest discover tests
```

Or you can run the test file directly:

```bash
python tests/test_fibonacci.py
```

## Test Coverage

The tests cover:

1. Basic functionality of the `fibonacci()` function:
   - Edge cases (0, 1)
   - Small values (2-5)
   - Larger values
   - Error handling for negative inputs

2. Functionality of the `fibonacci_sequence()` function:
   - Empty sequence
   - Sequences of various lengths
   - Error handling for negative inputs