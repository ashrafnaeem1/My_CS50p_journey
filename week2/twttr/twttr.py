"""A program to remove all vowels from given string."""


def main():
    """Inputs text, outputs vowelless text after processing."""
    text = input("Input: ")
    vowelless_text = get_vowelless(text)
    print(f"Output: {vowelless_text}")


def get_vowelless(text: str) -> str:
    """Returns a copy of text that does not contain any vowel."""
    vowels = set("aeiouAEIOU")
    vowelless_text = ""
    for ch in text:
        if ch not in vowels:
            vowelless_text += ch
    return vowelless_text


if __name__ == "__main__":
    main()
