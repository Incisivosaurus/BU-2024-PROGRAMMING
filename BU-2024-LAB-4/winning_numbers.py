def winning_numbers(user_list, winning_list):
    """
    This function checks if the user's numbers match the predefined winning numbers.

    Parameters:
    user_list (list): A list of three integers representing the user's chosen numbers.
    winning_list (list): A list of integers representing the winning numbers.

    Returns:
    str: A string indicating the prize won:
        - "First" if all three numbers match the winning numbers.
        - "Second" if two numbers match the winning numbers.
        - "Third" if one number matches the winning numbers.
        - "No" if none of the numbers match the winning numbers.

    Example:
    --------
    winning_list = [5, 14, 17]
    user_list = [3, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since one number, 5, matches the winning numbers)

    user_list = [14, 5, 10]
    result = winning_numbers(user_list, winning_list)
    # Output: "Third" (since two numbers, 14 and 5, match the winning numbers)

    The function also prints a message indicating the prize won.
    """

    # Function implementation here ...
    prize = "No"
    
    # If the user tries to cheat but using more than 3 numbers, they're automatically disqualified
    if len(user_list) > 3:
        return prize
    
    matching_values = set(winning_list).intersection(user_list)

    if len(matching_values) == 3:
        prize = "First"
    elif len(matching_values) == 2:
        prize = "Second"
    elif len(matching_values) == 1:
        prize = "Third"
        
    # Print the result
    print(f"Congratulations, you won {prize} prize!")

    return prize


if __name__ == "__main__":
    winning_list = [5, 14, 17]

    winning_numbers([3, 5, 10], winning_list)
    winning_numbers([14, 5, 10], winning_list)
