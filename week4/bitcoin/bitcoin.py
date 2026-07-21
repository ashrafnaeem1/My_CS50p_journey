"""A program to convert bitcoins to US dollars, using data fetched in realtime."""

import sys
import requests


def main():
    """UI/UX and main logic of the program."""
    try:
        r = requests.get(
            r"https://rest.coincap.io/v3/assets/bitcoin?apiKey=1a983a49e41426312b79b8a6858f9fa4c60b00bfb55555282403e2b486be60e7",
            timeout=100
        )
    except requests.RequestException as e:
        sys.exit("Something went wrong while requesting a needed json file."
                 +
                 e.args[0])
    json_content = r.json()  # r.json() returns a dict
    factor = float(json_content["data"]["priceUsd"])

    try:
        bitcoins = float(sys.argv[1])
    except ValueError as e:
        sys.exit(e.args[0]
                 +
                 "\n[Mostly input was not a valid number."
                 +
                 "Try inputing a decimal or integer value.]\n")
    except IndexError as e:
        sys.exit(e.args[0]
                 +
                 "\n[Most likely you gave the wrong command-line arguments.\n"
                 +
                 "OR you didn't give any command-line arguments.]\n")

    usd = bitcoins * factor
    print(f"${usd:,.4f}")


if __name__ == "__main__":
    main()
