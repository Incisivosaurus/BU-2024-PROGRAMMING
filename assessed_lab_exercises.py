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
        result = num1 + num2 # If the operator is +, add the 2 numbers together
    elif operator == "-":
        result = num1 - num2 # If the operator is -, subtract num2 from num1
    elif operator == "*":
        result = num1 * num2 # If the operator is *, multiply the 2 numbers together
    elif operator == "/": # If the operator is /, divide num1 by num2
        if num2 == 0: # You cannot divide by zero, so check if num2 is zero
            print(f"Mathematical error detected: division by zero") # If num2 is zero, print a division by zero message

            return # Return early, doing nothing if num2 is zero
        
        result = num1 / num2
    elif operator == "%": # If the operator is %, get the remaining value of num1 being divided by num2
        if num2 == 0: # You cannot divide by zero, so check if num2 is zero
            print(f"Mathematical error detected: division by zero") # If num2 is zero, print a division by zero message

            return # Return early, doing nothing if num2 is zero
        
        result = num1 % num2
    elif operator == ">":
        result = num1 > num2 # If the operator is >, check if num1 exceeds num2
    elif operator == ">=":
        result = num1 >= num2 # If the operator is >=, check if num1 exceeds or is equal to num2
    elif operator == "<":
        result = num1 < num2 # If the operator is <, check if num1 is less than num2
    elif operator == "<=":
        result = num1 <= num2 # If the operator is <=, check if num1 is less than or equal to num2
    else:
        print("Invalid operator.") # If the operator isn't any of the ones above, just print an error message

    if result is not None:
        print(f"The result is: {result}") # If there is a successful mathematical result, print what it is

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

    biggest = num1 # Make a default biggest number set to num1

    if num2 > biggest and num2 >= num3:
        biggest = num2 # If num2 is bigger than the current biggest (num1) and bigger than or equal to num3, then this is the new biggest
    elif num3 > biggest and num3 >= num2:
        biggest = num3 # If num3 is bigger than the current biggest (num1) and bigger than or equal to num2, then this is the new biggest

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
    prize = "No" # The default value, no prize
    
    # If the user tries to cheat but using more than 3 numbers, they're automatically disqualified
    if len(user_list) > 3:
        return prize
    
    # Since intersect makes a new set of values that are mutually present in both sets, this will allow me to detect correct guesses
    matching_values = set(winning_list).intersection(user_list)

    if len(matching_values) == 3:
        prize = "First" # If you have 3 mutual values in the 2 sets, you get first place
    elif len(matching_values) == 2:
        prize = "Second" # If you have 2 mutual values in the 2 sets, you get second place
    elif len(matching_values) == 1:
        prize = "Third" # If you have 1 mutual values in the 2 sets, you get third place
        
    # Print the result
    print(f"Congratulations, you won {prize} prize!")

    return prize


def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """

    # Function implementation here ...
    # Zero and One are not primes, so we can early return for those
    if num == 0 or num == 1:
        return False

    # Loop over all values starting from 2 up to whatever value is before num
    for i in range(2, num):
        # Check if num being divided by i has a remainder, if it does then it's not prime
        if num % i == 0:
            return False

    # If the loop doesn't determine num is non-prime, return True
    return True


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


def calculate_weekly_pay(hours_worked):
    """
    Calculate the weekly pay for an employee based on the number of hours worked.
    
    Parameters:
    hours_worked (int): The total number of hours worked by the employee in a week.
    
    Returns:
    float: The total weekly pay.
    """
    regular_rate = 12  # £12 per hour for up to 35 hours
    overtime_rate = 18  # £18 per hour for hours worked beyond 35 hours
    standard_hours = 35  # Threshold for regular pay



    # Function implementation here ...
    overtime_hours = hours_worked % standard_hours # Remainder after taking away the standard hours worked
    standard_hours = hours_worked - overtime_hours # Calculate how many standard hours worked
    standard_pay = regular_rate * standard_hours # Calculate pay using standard hours
    overtime_pay = overtime_rate * overtime_hours # Calculate pay using overtime hours
    total_pay = standard_pay + overtime_pay # Add both standard pay and overtime pay together to get the total

    return total_pay


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

    boolean = is_prime(5)   # returns True

    print(boolean)

    print(are_anagrams("listen", "silent"))  # Expected output: True
    print(are_anagrams("hello", "world"))    # Expected output: False

    numbers = [10, 20, 30, 40, 50]

    print("The average is:", calculate_average(numbers))  # Expected output: The average is: 30.0

    overtime_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
    
    print(overtime_pay)
