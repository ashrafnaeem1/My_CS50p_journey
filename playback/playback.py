"""A program that replaces the 'spaces' from text and replaces it with '...'."""


def main():
    """input text, replace 'spaces' with '...' and output that."""
    print("Enter your sentence below: ")
    text = input()
    modified_text = text.replace(" ", "...")
    print(modified_text)


if __name__ == "__main__":
    main()
