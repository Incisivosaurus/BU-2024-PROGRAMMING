def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    
    first = "" # Define new variable for storing a stripped down str1
    second = "" # Define new variable for storing a stripped down str2

    # Iterate over str getting each individual letter one by one
    for letter in str1:
        # Check if the letter is alphabetical
        if letter.isalpha():
            first += letter.lower() # If the letter is alphabetical, add it to the new first variable and force it to be lowercase

    # Iterate over str getting each individual letter one by one
    for letter in str2:
        # Check if the letter is alphabetical
        if letter.isalpha():
            second += letter.lower() # If the letter is alphabetical, add it to the new first variable and force it to be lowercase

    return sorted(first) == sorted(second)


if __name__ == "__main__":
    ## Example 
    print(are_anagrams("listen", "silent"))  # Expected output: True
    print(are_anagrams("hello", "world"))    # Expected output: False
