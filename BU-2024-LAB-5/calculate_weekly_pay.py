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
    

if __name__ == "__main__":
    # # Code Example
    overtime_pay = calculate_weekly_pay(36) # return 438 i.e, 438 in pounds per week.
    print(overtime_pay)
