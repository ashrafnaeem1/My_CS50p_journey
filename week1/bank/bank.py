"""A program that prints total recievable amount from bank
   when the bank makes a mistake of Not greeting with Hello.

   * A 'hello' greeting amounts to no recieved payment.
   * A greeting starting with 'h' except 'hello' amounts to $20.
   * A greeting not starting with 'h' amounts to $100."""


def main():
    """Handles input and output and uses helpers for processing."""
    greeting = input("Greeting: ")
    receivable = int(get_receivable_amount(greeting))
    print(f"${receivable}")


def get_receivable_amount(greeting: str):
    """ Returns the receivable amount corresponding to greeting.

    * A 'hello' greeting amounts to no recieved payment.
    * A greeting starting with 'h' except 'hello' amounts to $20.
    * A greeting not starting with 'h' amounts to $100."""
    greeting_clean = greeting.strip().lower()

    if greeting_clean.startswith("hello"):
        return 0
    elif greeting_clean.startswith("h"):
        return 20

    return 100


if __name__ == "__main__":
    main()
