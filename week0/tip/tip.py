"""A program that outputs corresponding tip for a given input amount.
   Note that basic structure was pre-written by the CS50p staff."""


# pre-implemented by CS50 staff.
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(
        input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# My implementations, note that the function signature
# was provided by CS50 staff.
def dollars_to_float(d):
    """Remove prefix dollar sign and convert the number to float.

       Assumes that d is an str starting with a $ sign, and the
       remaining string is convertible to float."""
    d = float(d.removeprefix("$"))
    return d


def percent_to_float(p):
    """Convert percentage to float by changing percentage to
       corresponding decimal values between (and including) 0 and 1."""
    p = float(p.removesuffix("%")) / 100
    return p


# below line was provided by CS50 staff.
main()
