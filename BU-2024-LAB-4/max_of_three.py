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

# # You are out of the body function where you can test your code.
# Example usage:
if __name__ == "__main__":
    maximum = max_of_three(10, 20, 30)
    print(maximum, "is the maximum")
