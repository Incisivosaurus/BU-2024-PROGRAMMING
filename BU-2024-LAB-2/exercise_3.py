numbers = [4, 3, 5, 1]
numbers_size = len(numbers)

for i in range(numbers_size - 1):
    smallest_index = i

    for j in range(i + 1, numbers_size):
        if numbers[j] < numbers[smallest_index]:
            smallest_index = j

    numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]

print(numbers)
