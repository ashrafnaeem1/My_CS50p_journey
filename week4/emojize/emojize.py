"""A program that inputs emoji codes and outputs respective emojis."""
import emoji as emj


def main():
    """input text, process, and print emojized text.

    Prints f"Unexpected exception: {`e`}" on any exception."""
    try:
        text = input("Input: ").strip().lower()
        emojized_text = alias_supported_emojize(text)
    except Exception as e:
        print(f"Unexpected exception: {e}")
        return

    print("Output:", emojized_text)


def alias_supported_emojize(text: str) -> str:
    """Uses emoji.emojize() to return a copy of text with
    emoji codes replaced with emojis.

    Additionally supports aliases."""
    emojized_text_normal = emj.emojize(text)
    emojized_text_with_emojized_aliases = (
        emj.emojize(emojized_text_normal, language="alias"))

    return emojized_text_with_emojized_aliases


if __name__ == "__main__":
    main()
