""" a program that prompts the user for a vanity plate and then
    output Valid if meets all of the requirements of a vanity plate
    or Invalid if it does not.
"""


def main():
    """Inputs plate id, outputs its validity after validation.

    main() function was provided by CS50p and is untouched,
    apart from this docstring."""
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """Checks if a plate is valid as per CS50p rules. Signature for this
    function was provided by CS50p and is kept as it is. My implementation
    adds code for it alongwith helper functions.

    See [CS50p: Vanity Plates](https://cs50.harvard.edu/python/psets/2/plates/)"""

    length = len(s)
    min_length, max_length = 2, 6

    # Rule: length should be in interval [2, 6]
    curr_res = is_length_in_range(min_length, max_length, length)
    if not curr_res:
        return False

    # Rule: Must only start with two alphabets atleast.
    curr_res = curr_res and check_starts_with_two_alphabets(s)
    if not curr_res:
        return False

    # Rule: Must not contain whitespaces or punctuation.
    # (actually, must only contain alpha-numeric characters.)
    curr_res = curr_res and s.isalnum()
    if not curr_res:
        return False

    first_digit = get_first_digit(s)

    # Rule: first number should not start with a zero.
    # (that is, effectively, first digit in plate should not be zero.)
    curr_res = curr_res and (first_digit != 0)
    if not curr_res:
        return False

    # Rule: numbers cannot appear anywhere, except at the two ends.
    curr_res = (
        curr_res and not check_number_except_at_ends(s, length)
    )
    if not curr_res:
        return False

    return curr_res


def is_length_in_range(
        min_length: int,
        max_length: int,
        length: int | None = None,
        s: str | None = None
) -> bool:
    """Checks if `length` is in interval [`min_length`, `max_length`].

    If no `length` is provided or `length` is None, it uses `len(s)` to
    get the length.

    If neither `s` nor `length` is provided, raises ValueError."""
    if not length:
        if s is None:
            raise ValueError(
                "Provide either a str `s` or int `length` atleast.")
        else:
            length = len(s)
    return min_length <= length <= max_length


def check_starts_with_two_alphabets(s: str) -> bool:
    """Checks if both of the first two characters are alphabets.

    Raises ValueError if length of `s` is less than two."""

    result: bool
    if len(s) >= 2:
        if s[0].isalpha() and s[1].isalpha():
            result = True
        else:
            result = False
    else:
        raise ValueError(
            f"Length of `s` '{s}' is smaller than two.")

    return result


def get_first_digit(s: str) -> int | None:
    """Returns the first digit in `s`."""
    first_digit: int | None = None
    for ch in s:
        if ch.isnumeric():
            first_digit = int(ch)
            break
    return first_digit


def check_number_except_at_ends(s: str,
                                length: int | None = None) -> bool:
    """Checks if there are numbers at the two ends of `s`."""

    if not length:
        length = len(s)

    terminal_numbers_stripped = strip_terminal_numbers(s, length)
    first_middle_number = get_first_digit(terminal_numbers_stripped)

    # print(f"first middle number is {first_middle_number}")
    has_middle_number: bool
    if first_middle_number:
        has_middle_number = True
    else:
        has_middle_number = False
    # print(f"has middle number(s): {has_middle_number}")
    return has_middle_number


def strip_terminal_numbers(s: str,
                           length: int | None = None) -> str:
    """Returns a copy of `s` with terminal numbers stripped
    from both the ends."""

    if not length:
        length = len(s)
    left = 0
    new_length = length
    for ch in s:
        if ch.isnumeric():
            left += 1
        else:
            break
    for ch in reversed(s):
        if ch.isnumeric():
            new_length -= 1
        else:
            break
    terminal_numbers_stripped = s[left:new_length]
    # print(f"stripped is {terminal_numbers_stripped}")
    return terminal_numbers_stripped


if __name__ == "__main__":
    main()
