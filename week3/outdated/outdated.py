"""A program that takes US format date and prints ISO format equivalents."""

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    """UI/UX and main logic of the program."""
    while True:
        try:
            # titlecase to perform comparision with MONTHS list.
            date_str = input("Date: ").strip().title()

            if not date_str.isalnum():
                raise ValueError(f"Unsupported symbols in date: {date_str}.")

            if "/" in date_str:
                date_parts = date_str.split("/")
                # all parts must be numeric
                if not all(part.isnumeric() for part in date_parts):
                    raise ValueError("Numeric format must use numbers only.")
            elif " " in date_str:
                date_parts = date_str.split(" ")
                # we must check if day has a comma for proper formatting.
                day_placeholder = date_parts[1]
                if day_placeholder[-1] == ",":
                    day_placeholder = day_placeholder.removesuffix(",")
                    date_parts[1] = day_placeholder
                else:
                    raise ValueError(
                        "Unsupported format, missing a comma after value of day.")
            else:
                raise ValueError(
                    "Unsupported format. Use only supported US formats for input.")

            if len(date_parts) != 3:
                raise ValueError(
                    "The date must only contain month, day and year.")

            # unpack date_parts into variables.
            month, day, year = date_parts

            if month.isalpha():
                if month in MONTHS:
                    # list is off by 1, list start is 0 which month start is 1.
                    month = MONTHS.index(month) + 1
                else:
                    raise ValueError("Not a valid month.")
            elif month.isnumeric():
                # now month is definitely numeric if month was valid, else reprompt!
                month = int(month)
            else:
                raise ValueError("Month must be a number.")

            if not (1 <= month <= 12):
                raise ValueError(
                    "Month is out of range. Allowed 1 to 12 only (1 and 12 included.)")

            if not day.isnumeric():
                raise ValueError(
                    "Day must be a number, between 1 to 31 (1 and 31 included.)")
            day = int(day)
            if not (1 <= day <= 31):
                raise ValueError(
                    "Day is out of range. Allowed 1 to 31 only (1 and 31 included.)")

            if not year.isnumeric():
                raise ValueError("Year must be number.")

            year_fmt, month_fmt, day_fmt = ["yyyy", "mm", "dd"]
            year = get_formatted_num_str(year, len(year_fmt))
            day = get_formatted_num_str(day, len(day_fmt))
            month = get_formatted_num_str(month, len(month_fmt))

            print(year, month, day, sep="-")
            break  # while
        except ValueError:
            continue


def get_formatted_num_str(num: str | int,
                          format_to_digits: int) -> str:
    """Returns an str representing `num` but padded with zeros
    to match formatting with `format_to_digits` if required."""

    if isinstance(num, str):
        if not num.isnumeric():
            raise ValueError("given argument is not a number.")

    num = int(num)
    # The '0' means "pad with zeros"
    return f"{num:0{format_to_digits}}"


if __name__ == "__main__":
    main()
