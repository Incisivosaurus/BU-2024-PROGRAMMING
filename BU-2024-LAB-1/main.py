import random

questions = [
    "What is your favourite animal?",
    "What is your favourite movie?",
    "Where were you born?"
]

responses = [
    "That's cool",
    "Interesting",
]


def main():
    for question in questions:
        answer = input(question + " ")

        print(random.choice(responses), end="\r\n\r\n")


if __name__ == "__main__":
    main()
