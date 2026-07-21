"""A program to get the calories of eligible fruits. Ignores input
   if not eligible.
   Based on:
   https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/raw-fruits-poster-text-version-accessible-version
"""


def main():
    """Inputs item, prints calories."""
    item = (input("Item: ")
            .strip()
            .lower())
    calories = get_calories(item)
    if calories:
        print(f"Calories: {calories}")


def get_calories(item: str) -> int | None:
    """Returns the corresponding calorie to `item`.

    Returns `None` if `item` is not found."""
    calories_chart = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydrew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 50,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    calories = calories_chart.get(item)
    return calories


if __name__ == "__main__":
    main()
