def fibonacci(n):
    """
    Calculate the nth Fibonacci number iteratively.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
    
    Returns:
        int: The nth Fibonacci number
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b


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
