def calculator(num1, num2, operator):
    """
    This function performs basic arithmetic and comparison operations on two numbers.

    Parameters:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    operator (str): A string representing the operation to perform. The valid operators are:
        - "+" for addition
        - "-" for subtraction
        - "*" for multiplication
        - "/" for division
        - "%" for modulus
        - ">" for greater than comparison
        - ">=" for greater than or equal to comparison
        - "<" for less than comparison
        - "<=" for less than or equal to comparison

    Returns:
    result: The result of the arithmetic operation or comparison. The type of the result depends on the operator:
        - int or float for arithmetic operations
        - bool for comparison operations

    Example Usage:
    --------------
    calculate(4, 5, "*")  # Output: The result is: 20
    calculate(10, 2, "/")  # Output: The result is: 5.0
    calculate(7, 7, ">=")  # Output: The comparison result is: True

    Note:
    -----
    - If division by zero is attempted, the function prints an error message and does not return a result.
    - If an invalid operator is provided, the function prints an error message and does not return a result.
    """
    result = None

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print(f"Mathematical error detected: divison by zero")

            return
        
        result = num1 / num2
    elif operator == "%":
        if num2 == 0:
            print(f"Mathematical error detected: divison by zero")

            return
        
        result = num1 % num2
    elif operator == ">":
        result = num1 > num2
    elif operator == ">=":
        result = num1 >= num2
    elif operator == "<":
        result = num1 < num2
    elif operator == "<=":
        result = num1 <= num2
    else:
        print("Invalid operator.")

    if result is not None:
        print(f"The result is: {result}")

    return result


def max_of_three(num1, num2, num3):
    """
    This function takes three integers as input and returns the maximum of the three given numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.

    Returns:
    int: The maximum of the three numbers.
    """
    # Hint: you are required to make use of maximum variable that is returned by the function below.
    # Complete your code implementation here...

    biggest = num1

    if num2 > biggest and num2 >= num3:
        biggest = num2
    elif num3 > biggest and num3 >= num2:
        biggest = num3

    # We could just do max(num1, num2, num3) but we've been told to not use methods that we haven't been taught in lesson, so to be safe, I'm not using it
    return biggest


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


## Run the example
if __name__ == "__main__":
    calculator(4, 5, "*")  # Output: The result is: 20
    calculator(10, 2, "/")  # Output: The result is: 5.0
    calculator(7, 7, ">=")  # Output: The comparison result is: True

    maximum = max_of_three(10, 20, 30)
    
    print(maximum, "is the maximum")

    winning_list = [5, 14, 17]

    winning_numbers([3, 5, 10], winning_list)
    winning_numbers([14, 5, 10], winning_list)
