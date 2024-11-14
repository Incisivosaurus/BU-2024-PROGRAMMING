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

## Run the example
if __name__ == "__main__":
    calculator(4, 5, "*")  # Output: The result is: 20
    calculator(10, 2, "/")  # Output: The result is: 5.0
    calculator(7, 7, ">=")  # Output: The comparison result is: True
