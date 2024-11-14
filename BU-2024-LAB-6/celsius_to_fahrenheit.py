def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32 # Convert celsius to fahrenheit using the standard formula x * 9 / 5 + 32

    return fahrenheit

if __name__ == "__main__":
    print(celsius_to_fahrenheit(32) == 89.6) # Result should be true
    print(celsius_to_fahrenheit(27.5) == 81.5) # Result should be true
    print(celsius_to_fahrenheit(35) == 90) # Result should be false
