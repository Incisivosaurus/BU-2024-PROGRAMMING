def remove_duplicates(numbers):
    """
    Removes duplicates from a list of numbers and returns a new list with unique elements.

    Parameters:
    ----------
    numbers : list
        A list of numbers which may contain duplicate values.

    Returns:
    -------
    list
        A new list with duplicate values removed.
    
    Example:
    --------
    remove_duplicates([1, 2, 2, 3, 4, 4, 5])  # Output: [1, 2, 3, 4, 5]
    """
    # Hint: Convert the list to a set to remove duplicates, then convert it back to a list
    # List --> Set (remove duplicates) --> List (return the list)
    # Write your code here...

    unique_numbers = set(numbers)

    return list(unique_numbers)

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
