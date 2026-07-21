"""An implementation of
  [Adieu, Adieu](https://cs50.harvard.edu/python/psets/4/adieu/)"""

# needed for str to inflect.Word conversion, for inflect's join() function
from typing import cast
import inflect as inf

# needed for using inflect's join()
eng = inf.engine()


def main():
    """input names and say adieu to them."""
    names = get_names("Name: ")
    names_listed_with_proper_conj = get_names_listed_with_proper_conj(names)
    print("Adieu, adieu, to", names_listed_with_proper_conj)


def get_names(common_prompt: str) -> list[str]:
    """inputs names until EOF is given.

    Returns a list of the names."""
    names: list[str] = []
    while True:
        try:
            name = input(common_prompt).strip()
            if name:
                names.append(name)
        except EOFError:
            break
    print(names)
    return names


def get_names_listed_with_proper_conj(names: list[str]) -> str:
    """Recieves a list of names and converts it into an str
    representing a comma separated list of names.
    """
    if not names:
        raise ValueError("Provided list should not be empty.")

    # Note: str can be more than one words, but inflect.Word
    # can only be one word long (or empty).
    # hence str to Word casting is not safe in general.
    # however for this problem, input names will all be one word in length
    # hence we can cast str to Word without worrying.
    # cast() has been used to perform an explicit casting.
    names_listed_with_proper_conj = eng.join(cast(list[inf.Word], names))

    return names_listed_with_proper_conj


if __name__ == "__main__":
    main()
