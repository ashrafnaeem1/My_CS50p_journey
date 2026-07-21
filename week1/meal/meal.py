"""A program that tells whether it is time for
   breakfast, lunch or dinner.

   Note: this solution is built on top of CS50p's
   mandated structure for this problem which requires
   signatures for a main() and a convert(),
   with a few conditions mandated for convert() function.
   See [CS50p: Meal Time](https://cs50.harvard.edu/python/psets/1/meal/)"""


def main():
    """Defines time windows, inputs current time and
       prints name of the time window (breakfast, lunch or dinner)."""

    breakfast_window = {
        "start": "7:00",
        "end": "8:00"
    }

    lunch_window = {
        "start": "12:00",
        "end": "13:00"
    }

    dinner_window = {
        "start": "18:00",
        "end": "19:00"
    }

    current_time = convert(input("What time is it? "))

    match check_meal_time(current_time,
                          breakfast_window,
                          lunch_window,
                          dinner_window):
        case "breakfast":
            print("breakfast time")
        case "lunch":
            print("lunch time")
        case "dinner":
            print("dinner time")


def convert(time):
    """Converts 24-hour time to its float counter part
    representing hours as float.

    Eg. 7:30 returns 7.5 and 23:15 returns 23.25

    (30 min = 0.5 hour, 15 min = 0.25 hour)"""

    parts = time.split(":")
    hours = float(parts[0])
    minutes = float(parts[1])

    decimal_time = hours + (minutes/60)
    return decimal_time


def check_meal_time(current_time: float,
                    breakfast_window: dict[str, str],
                    lunch_window:     dict[str, str],
                    dinner_window:    dict[str, str]) -> str | None:
    """Returns the meal time to which current_time belong to
       based on meal windows provided.

       Meal windows are to be provided as dictionaries and each should
       have a "start" key and an "end" key. Value to each key is an str
       representing a valid time in "d:dd" or "dd:dd" format, where
       d is a digit and time is in 24 hour format.
       """

    for meal_time, window in zip(["breakfast", "lunch", "dinner"],
                                 [breakfast_window,
                                  lunch_window,
                                  dinner_window]):
        if convert(window["start"]) <= current_time <= convert(window["end"]):
            return meal_time

    return None


if __name__ == "__main__":
    main()
