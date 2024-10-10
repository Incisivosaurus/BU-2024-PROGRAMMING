a = 11
a += 5
a -= 5
a *= 5
a /= 5
a //= 5
a **= 5
a %= 5

b = 5

print(f"Value of 'a'={a}, type of 'a'={type(a)}")
print(f"a < b={a < b}")

unit_name = "Level 4 Programming"

print(f"{unit_name[0]}{unit_name[3]}{unit_name[8]}")

greeting_string = "Welcome to Programming unit! This is level 4 unit :)"

print(f"{greeting_string[0]}{greeting_string[4]}")
print(f"{greeting_string[0:5]}")
print(f"{greeting_string[-1]}")
print(f"{greeting_string[-7:-4]}") # -7 will start at the 7th last character, and -3 will get all characters 3rd from last.

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
