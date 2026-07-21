"""Program that takes grocery items and prints them back with added enumeration
   and removed repeatition, while also capitalising output. """


def main() -> None:
    """inputs grocery items and prints them with serial number
    until EOF is given. Removes repeatation."""
    is_running = True
    grocery_dict: dict[str, int] = {}

    while is_running:
        # input is case-INsensitive, and we need titlecase str anyway.
        try:
            item = input().strip().upper()
            if item in grocery_dict:
                grocery_dict[item] += 1
            else:
                grocery_dict.update({item: 1})
        except EOFError:
            is_running = False

    for item in sorted(grocery_dict.keys()):
        print(f"{grocery_dict[item]} {item}")


if __name__ == "__main__":
    main()
