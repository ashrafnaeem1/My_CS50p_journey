"""A program to conver emoticons {':)', ':('} with emojis"""


def main():
    """Input text and print it after converting its emoticons to emoji."""
    print("Enter some text below: ")
    text = input()
    print(convert(text))


def convert(text: str):
    """Converts emoticons to emojis"""
    faces = {
        ":)": "🙂",
        ":(": "🙁"
    }

    modified_text = text
    for emoticon in faces:
        emoji = faces[emoticon]
        modified_text = modified_text.replace(emoticon, emoji)

    return modified_text


if __name__ == "__main__":
    main()
