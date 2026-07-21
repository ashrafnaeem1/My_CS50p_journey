"""A program that uses figlet library to output FIGLET text."""

# for parsing -f and --font
import argparse
import random
import sys
# Observed a lot of repeats, so using time to randomise further.
import time

from pyfiglet import Figlet
figlet = Figlet()


def main():
    """input text, output figlet text."""
    fontlist = figlet.getFonts()
    # using the time as seed, hopefully will give better randomness
    random.seed(time.time())

    font = ""
    num_passed_args = len(sys.argv) - 1
    # i no passed args i.e. zero args
    if not num_passed_args:
        font = random.choice(fontlist)
    elif num_passed_args == 2:
        try:
            args = get_parsed_args()
            font = args.font
            if font not in fontlist:
                raise ValueError(
                    "Invalid font. Font must be supported by pyfiglet.")
        except ValueError as e:
            sys.exit(e.args[0])
    else:
        sys.exit(
            "Program expects either zero arguments or two exactly arguments."
        )
    figlet.setFont(font=font)
    text = input("Input: ")
    rendered_text = figlet.renderText(text)
    print(rendered_text)


MSG_EXPLAIN_VALID_SYNTAXES = ("valid syntaxes are: \n"
                              "---\n"
                              "python figlet.py\n"
                              "Asks for input, returns figlet text with a random font.\n"
                              "python figlet.py -f valid_font\n"
                              "Asks for input, returns figlet text with given font.\n"
                              "python figlet.py --font valid_font\n"
                              "Asks for input, returns figlet text with given font.\n"
                              "---\n"
                              "valid_font must be a font supported by pyfiglet.\n")


def get_parsed_args() -> argparse.Namespace:
    """Returns parsed arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--font")

    args, unknown = parser.parse_known_args()

    # actually main will also handle no font value case (and do it first.)
    # so we only really need to handle random stuff like (-t pikachu)
    # striped down the `if "-f" in unknown` guard.
    if unknown:
        raise ValueError("Passed invalid arguments.\n"
                         +
                         MSG_EXPLAIN_VALID_SYNTAXES)
    return args


if __name__ == "__main__":
    main()
