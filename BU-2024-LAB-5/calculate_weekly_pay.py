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
	regular_hours = min(hours_worked, standard_hours) # Only get a maximum of 35 hours for regular hours
	overtime_hours = max(0, hours_worked - standard_hours) # Find the overtime hours by subtracting the hours worked by the standard hours, never going below 0

	# Multiply the regular hours by the regular rate, then add the overtime hours multiplied by the overtime rate together
	return regular_hours * regular_rate + overtime_hours * overtime_rate
    

if __name__ == "__main__":
    # # Code Example
    overtime_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
    print(overtime_pay)
