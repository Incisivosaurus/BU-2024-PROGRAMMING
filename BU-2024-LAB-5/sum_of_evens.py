def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """

    # Function implementation here ...
    total = 0 # Our variable for keeping track of the total value

    # Loop over all numbers between min_value and max_value, to make it inclusive, we do + 1 at the end
    for i in range(min_value, max_value + 1):
        if i % 2 == 0: # Check if current value is even using modulo
            total += i # If the condition above is true, add the value to the total
    
    return total


if __name__ == "__main__":
    # # # Run code example
    min_value = 10
    max_value = 13
    result = sum_of_evens(min_value, max_value) # returns 22
    
    print(result)
