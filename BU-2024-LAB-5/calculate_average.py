def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers using a for loop.

    Parameters:
    ----------
    numbers : list
        A list of numerical values (int or float).

    Returns:
    -------
    float:
        The average of the numbers in the list. If the list is empty, returns None.

    Example:
    --------
    calculate_average([10, 20, 30, 40, 50])  # Output: 30.0
    """
    
    total = 0 # Define a variable for storing the sum of numbers (usually would use built-in sum() function)
    length = 0 # Define a variable for storing the amount of items in numbers (usually would use built-in len() function)

    # Function implementation here ...
    # Iterate over the items in numbers
    for number in numbers:
        total += number # Increase the value of total by the amount number is equal to
        length += 1 # Increase the value of length to update how many items we've iterated over

    # To calculate the mean of something you take the sum total and divide by the amount of items being taken into account
    return total / length


if __name__ == "__main__":
    # # Example usage
    numbers = [10, 20, 30, 40, 50]
    print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0
