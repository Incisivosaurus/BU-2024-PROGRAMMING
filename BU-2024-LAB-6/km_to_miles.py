def km_to_miles(kilometers):
    miles = kilometers * 0.62 # Convert kilometers to miles

    return round(miles, 3) # Round to the nearest 3 decimals


if __name__ == "__main__":
    print(km_to_miles(1) == 0.621) # Expected result is True
    print(km_to_miles(5) == 3.107) # Expected result is True
    print(km_to_miles(7) == 4.349) # Expected result is False
