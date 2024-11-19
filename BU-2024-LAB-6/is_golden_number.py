def is_golden_number(n):
	# Only accept positive values (anything above 0) and only accept values less than 1,000
	if n <= 0 or n >= 1000:
		return False

	# If (n - 1) ^ 2 is less than 1,000, then the product of any two integers (i, j) adding up to 'n' will also
	# be less than 1,000, thus not being divisible by 1,000 without a remainder
	if (n - 1) ** 2 < 1000:
		return False

	# Loop over all values between 2 (inclusive) and 'n' (exclusive)
	# We can start at 2 instead of 1 because 1 will never multiply to a number divisible by 1,000 as 'n' can only ever be less than 1,000
	for i in range(2, n):
		# There's no reason to loop over 'n' again, so we may as well limit it to the value 'i' is at (inclusively by adding +1).
		for j in range(2, i + 1):
			# If 'i' and 'j' equal exactly 'n' and can be cleanly divided by 1,000 without a remainder, return True
			if i + j == n and i * j % 1000 == 0:
				return True

	return False


if __name__ == "__main__":
	print(is_golden_number(65) == True) # Expected result is True
	print(is_golden_number(70) == True) # Expected result is True
	print(is_golden_number(61) == True) # Expected result is True
