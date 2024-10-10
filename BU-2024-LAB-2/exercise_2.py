while True:
    try:
        number = input("Number: ")

        cast_number = int(number)
    except ValueError:
        continue
    
    break

while True:
    try:
        digit_index = input("Digit Index: ")

        cast_digit_index = int(digit_index)
    except ValueError:
        continue
    
    break

real_digits = 0

for digit in number:
    try:
        is_int = int(digit)

        real_digits += 1

        if real_digits == cast_digit_index:
            print(f"Found #{digit_index} digit of {number} is {digit}")

            break
    except ValueError:
        continue
    