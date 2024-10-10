size = int(input("Size: "))

for i in range(1, size + 1):
    msg = (str(i) * i).rjust(size)

    print(f"{msg}")
