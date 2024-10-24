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

## Run the example
if __name__ == "__main__":
    calculator(4, 5, "*")  # Output: The result is: 20
    calculator(10, 2, "/")  # Output: The result is: 5.0
    calculator(7, 7, ">=")  # Output: The comparison result is: True
