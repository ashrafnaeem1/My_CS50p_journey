"""Program to output sum of inputted items when the user passes EOF,
   also prints a newline to seperate it's final output from terminal prompt."""


def main():
    """Keep inputting item and printing value sum until input EOF."""
    decimal_precision = 2
    menu = Menu()

    total = 0
    is_eof = False
    while not is_eof:
        try:
            item = input("Item: ").strip().title()
            value = menu.get_item_value(item)
            total += value
            if total:
                print(f"Total: ${total:.{decimal_precision}f}")
        except KeyError:
            # for this exercise, we are supposed to ignore such cases
            continue
        except EOFError:
            is_eof = True


class Menu:
    """Includes menu of items as `menu_dict` and methods to use that menu."""
    menu_dict: dict = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    def get_item_value(self, item: str) -> float:
        """Returns the value of item from menu.

        Raises `KeyError` if value is not available."""
        value = self.menu_dict.get(item)
        if not value:
            raise KeyError("Item is not in menu.")
        return value


if __name__ == "__main__":
    main()
