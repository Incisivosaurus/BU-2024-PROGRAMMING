def fuel_cost(distance_miles):
    MPG = 50 # Miles per gallon
    LITERS_PER_GALLON = 4.5 # Rough estimation on how many litres are in a gallon
    PRICE_PER_LITER = 1.49 # Price in pounds per liter

    # Calculate the total fuel cost by calculating the price per gallon traveled
    total_cost = PRICE_PER_LITER * distance_miles / MPG * LITERS_PER_GALLON

    return total_cost


if __name__ == "__main__":
    print(fuel_cost(50) == 6.705) # Expected result is True
    print(fuel_cost(33) == 4.4253) # Expected result is True
