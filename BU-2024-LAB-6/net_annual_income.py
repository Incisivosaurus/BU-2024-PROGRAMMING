def annual_net_income(gross_salary):
    if gross_salary >= 45_000:
        tax_rate = 0.5 # Apply 50% tax if your gross salary is above or equal to 45k
    elif gross_salary >= 30_000 and gross_salary < 45_000:
        tax_rate = 0.3 # Apply 30% tax if your gross salary is above or equal to 30k and less than 45k
    elif gross_salary < 30_000:
        tax_rate = 0.15 # Apply 15% tax if your gross salary is less than 30l
    
    # Calculate salary post tax reduction
    net_salary = gross_salary * (1 - tax_rate)

    return net_salary


if __name__ == "__main__":
    print(annual_net_income(60_000) == 30_000) # Expected result is True
    print(annual_net_income(30_000) == 21_000) # Expected result is True
    print(annual_net_income(20_000) == 17_000) # Expected result is True
