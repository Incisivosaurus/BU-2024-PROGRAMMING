def letter_occurrence(input_string):
    count = 0 # Variable to keep track of occurrences

    # Iterate over each individual character in the string
    for letter in input_string:
        # Add +1 to the count variable if the letter is equal to 'a' or 'A'
        if letter == "a" or letter == "A":
            count += 1

    return count # Return the stored amount of occurrences


if __name__ == "__main__":
    print(letter_occurrence("amazing") == 2) # Expected result is 2
    print(letter_occurrence("Always aim ambitiously") == 4) # Expected result is 4
