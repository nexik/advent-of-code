def load_data_for_day(day: str) -> list:
    with open(f"aoc/{day}/input.txt", 'r', encoding="utf-8") as lines:
        return lines.readlines()