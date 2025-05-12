def fibonacci(n):
    """
    Calculate the n-th Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-based)
    
    Returns:
        int: The n-th Fibonacci number
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Position must be a non-negative integer")
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


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