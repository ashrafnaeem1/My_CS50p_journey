"""A program that gives you math problems to solve, and provides
   your score at the end."""

import random


ALLOWED_LEVELS = (1, 2, 3)
NUM_PROBLEMS = 10


def main() -> None:
    """UI/UX and main logic of the program."""
    num_problems = NUM_PROBLEMS

    lvl = get_level()
    pairs: list[tuple[int, int]] = []
    for i in range(num_problems):
        pair: tuple[int, int] = (-1, -1)
        while True:
            try:
                pair = (generate_integer(lvl), generate_integer(lvl))
                break
            except ValueError:
                lvl = get_level()
                continue
        if pair == (-1, -1):
            print(f"Failed to generate {i}th pair.")
        else:
            pairs.append(pair)

    score = 0
    for pair in pairs:
        # each pair is (x, y)
        x = pair[0]
        y = pair[1]
        correct_sum = x + y

        loop_count = 0
        while True:
            loop_count += 1
            try:
                input_answer = input(f"{x} + {y} = ").strip()
                if input_answer.isdigit():
                    num = int(input_answer)
                    if num == correct_sum:
                        # only give point for correct answer.
                        score += 1
                        break
                if loop_count < 3:
                    print("EEE")
                    # no deduction for wrong answer.
                    continue
                else:
                    print("EEE")
                    print(f"{x} + {y} = {correct_sum}")
                    break
            except ValueError:
                continue
    print(f"Score: {score}")


def get_level() -> int:
    """inputs level."""
    allowed_levels = ALLOWED_LEVELS

    while True:
        try:
            lvl = int(input("Level: ").strip())
            if lvl in allowed_levels:
                break
        except ValueError:
            continue

    return lvl


def generate_integer(digits: int):
    """Generates an integer with given no. of digits."""
    allowed_levels = ALLOWED_LEVELS
    if digits not in allowed_levels:
        # ideally I think get_level should throw on this instead.
        # however cs50 is specifying to throw in generate_integer().
        # And autochecks fill fail if I don't throw ValueError **here**.
        raise ValueError(
            "Level is not valid. Valid levels are 1, 2 and 3 only.")

    if digits == 1:
        min_allowed_num = 0
    else:
        min_allowed_num = int("1" + ("0"*(digits-1)))

    max_allowed_num = int("9"*digits)
    num = random.randint(min_allowed_num, max_allowed_num)

    return num


def force_get_positive_int(prompt: str = "") -> int:
    """Forcefully inputs a positive integer and returns it."""
    num = -1
    while num <= 0:
        num = force_get_int(prompt)

    return num


def force_get_int(prompt="") -> int:
    """Forcefully inputs an integer and returns it."""
    while True:
        try:
            input_val = input(prompt).strip()
            num = int(input_val)
            # num is an int if code reaches here.
            break
        except ValueError:
            # if anything was wrong with input, code will force a retry
            continue

    return num


if __name__ == "__main__":
    main()
