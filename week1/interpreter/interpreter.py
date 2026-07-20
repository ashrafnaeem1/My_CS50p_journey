"""A program that calculates input expression and prints the result.

Assumptions:
1. User will only enter expressions of exact format `{lhs} {oper} {rhs}`.
2. {lhs} and {rhs} both represent valid floats.
3. {oper} is in ["+", "-", "*", "/"].
4. whenever {oper} is "/", {rhs} is non-zero.

Program will silently quit if these assumptions are not met, because CS50p
maintains the same assumptions for this problem with check50 which makes
any code dealing with other cases reduntant (and prone to failing on
automated checks)."""


import operator as op


def main():
    """Print instructions, input expression, calculate result and print it."""

    instructions = (
        "NOTE: Expression is calculated left to right, ignoring bodmas rule.\n"
        "Eg. 1 + 10 / 10 will give 1.1, whereas bodmas gives 2"
    )
    print(instructions)

    expression = input("Expression: ")
    result = calculate(expression)

    if result:
        print(f"{result:.{1}f}")


def calculate(expression: str) -> float | None:
    """Calculates the given expression and returns the result as float.

    Assumes that the expression provided contains

    Returns None when it fails to calculate expression."""

    parts = expression.split(" ")

    part = (part for part in parts)
    lhs = int(next(part))
    oper = next(part)
    rhs = int(next(part))

    return operate(oper, lhs, rhs)


def operate(oper: str, lhs: float, rhs: float) -> float | None:
    """Operates on lhs and rhs, and returns the result.

    Returns None if the operation is not supported."""
    operations = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "/": op.truediv
    }

    operation = operations.get(oper)

    if operation is None:
        return None

    return operation(lhs, rhs)


if __name__ == "__main__":
    main()
