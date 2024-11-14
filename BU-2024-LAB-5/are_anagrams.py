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

    # By alphabetically ordering the two strings, they should have the same result if they're actually anagrams
    # Making sure the strings are converted to lowercases so case sensitivity doesn't break anything
    return sorted(str1.casefold()) == sorted(str2.casefold())


if __name__ == "__main__":
    ## Example 
    print(are_anagrams("listen", "silent"))  # Expected output: True
    print(are_anagrams("hello", "world"))    # Expected output: False
