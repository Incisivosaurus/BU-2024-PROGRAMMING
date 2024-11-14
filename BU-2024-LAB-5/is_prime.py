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


if __name__ == "__main__":
    # # # Run code example
    boolean = is_prime(5)   # returns True

    print(boolean)
