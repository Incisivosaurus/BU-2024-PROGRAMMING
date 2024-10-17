import math

a = int(input("Side #1 Size: "))
b = int(input("Side #2 Size: "))
c = int(input("Side #3 Size: "))

s = (a + b + c) / 2
area = math.sqrt((s - a) * (s - b) * (s - c))

print(area)
