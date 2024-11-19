def find_maximum_difference(a, b):
    smallest_of_a = min(a) # Return which value is the smallest in the first list
    biggest_of_a = max(a) # Return which value is the biggest in the first list
    smallest_of_b = min(b) # Return which value is the smallest in the second list
    biggest_of_b = max(b) # Return which value is the biggest in the second list

    difference_of_a = biggest_of_a - smallest_of_b # Find the difference of the biggest value from the first list and the smallest value of the second list
    difference_of_b = biggest_of_b - smallest_of_a # Find the difference of the biggest value from the second list and the smallest value of the first list

    # Return the biggest value of the two
    return max(difference_of_a, difference_of_b)

if __name__ == "__main__":
    print(find_maximum_difference([1, 5, 600], [100, 7, 3, 29, 39])) # Expected output is 597
    print(find_maximum_difference([1, 5, 600], [100, 7, 3, 602, 39])) # Expected output is 601
    print(find_maximum_difference([100, 1], [99, 5])) # Expected output is 98