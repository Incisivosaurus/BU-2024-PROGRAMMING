import csv


def create_csv(filename, data):
    with open(filename, "w", newline="") as fd:
        writer = csv.writer(fd)
        writer.writerows(data)


def read_csv(filename):
    with open(filename, "r") as fd:
        reader = csv.reader(fd)

        for row in reader:
            print(row)


def append_to_csv(filename, data):
    with open(filename, "a", newline="") as fd:
        writer = csv.writer(fd)
        writer.writerows(data)


if __name__ == "__main__":
    content = [
        ["Name", "Age", "Grade"],
        ["Alice", 23, "A"],
        ["Bob", 22, "B"],
        ["Charlie", 24, "A"],
        ["David", 22, "C"],
        ["Eva", 23, "B"]
    ]

    filename = "students.csv"

    create_csv(filename, content)
    append_to_csv(filename, [["Jason", 21, "A"]])
    read_csv(filename)
