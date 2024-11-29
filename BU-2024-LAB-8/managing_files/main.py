from managing_files import *

if __name__ == "__main__":
    filename = "my_file.txt"

    write_to_file(filename, "This is my first file")
    append_to_file(filename, "I have added another text")
    append_to_file(filename, "I am adding for the third time a text to see what will happen inside the file")

    content = read_from_file(filename)

    print("All Lines:")
    print(content)
    print("First Line:")
    print(content.split("\n")[0])

    word_count = count_words(filename, "the")

    print("Word Count:")
    print(word_count)

    copy_contents(filename, "dest.txt")

    write_to_file(filename, "This is my fourth text")

    content = read_from_file(filename)

    print("All Lines:")
    print(content)

    print("Triangle Pattern:")

    triangle_pattern(filename, 4)

    content = read_from_file(filename)

    print(content)

    remove_file(filename)
