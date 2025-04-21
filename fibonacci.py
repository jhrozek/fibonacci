def fibonacci(n):
    raise NotImplementedError("Implement me")


def fibonacci_sequence(length):
    """
    Generate a list containing the Fibonacci sequence of the specified length.
    
    Args:
        length (int): Number of elements to generate
    
    Returns:
        list: A list of Fibonacci numbers
    
    Raises:
        ValueError: If length is negative
    """
    if length < 0:
        raise ValueError("Length must be a non-negative integer")
    
    return [fibonacci(i) for i in range(length)]


if __name__ == "__main__":
    # Example usage
    sequence = fibonacci_sequence(10)
    print(f"First 10 Fibonacci numbers: {sequence}")
