"""A program that prompts the user to insert a coin, one at a time,
   each time informing the user of the amount due.
   Once the user has inputted at least 50 cents,
   output how many cents in change the user is owed."""

INITIAL_AMOUNT_DUE = 50
ACCEPTED_COINS = (25, 10, 5)


def main():
    """Inputs insert coin, calculates amount due, calculates change owed,
       prints changed owed."""

    amount_due = INITIAL_AMOUNT_DUE
    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        insert_coin = get_int("Insert Coin: ")
        if insert_coin in ACCEPTED_COINS:
            amount_due -= insert_coin

    change_owed = abs(amount_due)
    print(f"Change Owed: {change_owed}")


def get_int(prompt: str = "") -> int:
    """Inputs an integer and returns it.

    Note: This function does not handle any exceptions by itself,
    as such program will terminate if user does not enter a
    integer. This is because CS50 directs that checks will only enter
    an integer."""
    return int(input(prompt).strip())


if __name__ == "__main__":
    main()
