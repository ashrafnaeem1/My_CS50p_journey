"""A program to convert camel case to snake case."""


def main():
    """input camelCase text, change to snake_case and print it."""
    camel_case = input("camelCase: ")
    snake_case = camel_case_to_snake_case(camel_case)
    print(f"snake_case: {snake_case}")


def camel_case_to_snake_case(camel_case: str) -> str:
    """Returns snake_case of given camelCased string `camel_case`."""
    length = len(camel_case)
    snake_case = ""
    # convert first char of `camel_case` to lowercase in `snake_case`
    if length > 0:
        snake_case = camel_case[0].lower()

    # handle rest of camel_case
    if length > 1:
        for ch in camel_case[1:]:
            sep = ""
            if ch.isupper():
                # if ch was upper, add a prefix _
                sep = "_"
            snake_case = sep.join([snake_case, ch.lower()])

    return snake_case


if __name__ == "__main__":
    main()
