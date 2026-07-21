"""A program to display fuel percentage. Displays E or F if empty or full
   respectively instead."""


def main():
    """UI/UX and helper calls."""
    min_almost_full = 99
    max_almost_empty = 1
    fraction = get_acceptable_fraction("Fraction: ")
    percentage = 100 * fraction
    output = ""
    if percentage >= min_almost_full:
        output = "F"
    elif percentage <= max_almost_empty:
        output = "E"
    else:
        output = str(round(percentage)) + "%"
    print(output, end="")


def get_acceptable_fraction(prompt: str) -> float:
    """Inputs a fraction and returns it.

    If fraction is not acceptable"""
    is_acceptable = False
    # these values are just to let python know
    # that numerator and denominator exist
    numerator: int = 1
    denominator: int = 0
    while not is_acceptable:
        try:
            given = input(prompt).strip()
            tokens = tokenize_non_negative_ints_and_slash(given)
            # tokens[0] is a str of non-negative integer and is the numerator
            # int() will throw ValueError if it is not so
            numerator = int(tokens[0])

            # tokens[1] is a slash
            _ = tokens[1]   # We don't need the slash.

            # tokens[2] is a str of non-negative integer and is the denominator
            # int() will throw ValueError if it is not so
            denominator = int(tokens[2])

            if denominator == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            if numerator > denominator:
                # dont throw anything!
                continue
            is_acceptable = True
        # cs50 automated checks are requiring me to throw exceptions
        # but to silently ignore those exceptions
        except (ValueError, ZeroDivisionError):
            is_acceptable = False
    try:
        fraction = float(numerator)/float(denominator)
    except Exception as e:
        print("Looks like my loop failed!")
        raise ValueError("Failed to correctly assign value to fraction") from e
    return fraction


def tokenize_non_negative_ints_and_slash(expr: str) -> tuple[str, str, str]:
    """Function to tokenize a non-negative fraction."""
    length = len(expr)
    for i, ch in enumerate(expr):
        slash_count = 0
        # if ch is Neither (a number) nor (a slash)
        # it uses de morgans law: a nor b = a' and b'
        # it follows from it that a' and b' = a nor b
        if ch == "/":
            slash_count += 1
        if slash_count > 1:
            raise ValueError(
                "Invalid format for a fraction: use only one slash.")
        if (not ch.isnumeric()) and (not ch == "/"):
            raise ValueError(
                "Invalid format for a fraction: use of unacceptable character."
            )
        if i == 0 and ch == "/":
            raise ValueError(
                "Invalid format for a fraction: no numerator given.")
        if i == (length - 1) and ch == "/":
            raise ValueError(
                "Invalid format for a fraction: no denominator given.")

    numerator = ""
    i = 0
    while i < length and expr[i].isnumeric():
        numerator = numerator + expr[i]
        i += 1

    denominator = ""
    i += 1  # to ignore the slash
    while i < length and expr[i].isnumeric():
        denominator = denominator + expr[i]
        i += 1

    return (numerator, "/", denominator)


if __name__ == "__main__":
    main()
