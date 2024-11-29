import os


def copy_contents(source, destination):
    if not file_exists(source):
        print(f"File \"{source}\" does not exist.")

        return
    
    source_content = read_from_file(source)

    write_to_file(destination, source_content, end="")


def triangle_pattern(filename, length):
    for i in range(length + 1, 0, -1):
        append_to_file(filename, "*" * i)


def count_words(filename, word):
    if not file_exists(filename):
        return 0
    
    content = read_from_file(filename)

    count = " ".join(content.split("\n")).split().count(word)

    return count
 

def file_exists(filename):
    try:
        with open(filename, "r"):
            return True
    except FileNotFoundError:
        return False


def write_to_file(filename, content, end="\n"):
    with open(filename, "w") as fd:
        fd.write(content + end)


def read_from_file(filename):
    if not file_exists(filename):
        return []
    
    with open(filename, "r") as fd:
        return fd.read()


def append_to_file(filename, content, end="\n"):
    with open(filename, "a") as fd:
        fd.write(content + end)


def remove_file(filename):
    if not file_exists(filename):
        return
    
    os.remove(filename)
