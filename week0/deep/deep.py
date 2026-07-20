"""A program that prompts the user for the answer to the
   Great Question of Life, the Universe and Everything, outputting
   Yes if the user inputs 42 or (case-insensitively) forty-two or forty two.
   Otherwise output No."""


def main():
    """Prompt the Great Question of Life, input answer,
       verify and print verfication result."""
    question = (
        "What is the Answer to the Great Question of Life, the Universe, and Everything? "
    )
    answer = input(question)

    if is_forty_two(answer.strip()):
        print("Yes")
    else:
        print("No")


def is_forty_two(s: str):
    """Checks if s is 42."""
    if s.lower() in ["42", "forty-two", "forty two"]:
        return True
    return False


if __name__ == "__main__":
    main()
