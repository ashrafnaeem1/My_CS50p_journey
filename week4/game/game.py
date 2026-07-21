"""An implementation of the famous High-Low Guessing Game,
   with an added mechanism of levels."""

import random


def main() -> None:
    """creates a secret number, inputs guesses,
    prints results until correct answer is input."""

    lvl = force_get_positive_int("Level: ")
    # randint INcludes both end points
    secret_num = random.randint(1, lvl)

    # get_num_in_range() includes only start, not the end
    # convention of this function is same as inbuilt range(start, end)
    guess: int | None = None
    while True:
        guess = force_get_positive_int("Guess: ")
        if guess < secret_num:
            print("Too small!")
            continue
        elif guess == secret_num:
            print("Just right!")
            break
        else:
            print("Too large!")
            continue


def force_get_positive_int(prompt: str = "") -> int:
    """Repeatedly takes input until the input is
    an str representing a positive integer. This
    function uses `force_get_int()` behind the scenes.

    Returns the final input as int."""
    num = -1
    while num <= 0:
        num = force_get_int(prompt)

    return num


def force_get_int(prompt: str = "") -> int:
    """Repeatedly takes input until the input is
    an str representing a integer.

    Returns the final input as int."""
    num: int | None = None
    while True:
        try:
            input_val = input(prompt).strip()
            num = int(input_val)
            # num is an int if code reaches here.
            break
        except ValueError:
            # if anything was wrong with input, code will force a retry
            continue
    if num is None:
        # if this happens, that will be concerning.
        raise ValueError("num was never assigned an integer value.")
    return num


if __name__ == "__main__":
    main()
