from aoc.helpers import load_data_for_day   
from pprint import pprint
import re

def part_one() -> int:
    lines = load_data_for_day('03')
    # remove trailing newline in each line
    lines = [line[:-1] for line in lines]

    return calculate_sum_of_gear_ratios(lines)

def part_two() -> int:
    return 0

def calculate_sum_of_gear_ratios(lines: list) -> int:
    sum = 0

    for index, _ in enumerate(lines):
        sum += calculate_gear_ratio(index, lines)

    return sum

def calculate_gear_ratio(line_number: int, lines: list) -> float:
    sum = 0
    line = lines[line_number]
    number_indexes = [m.start() for m in re.finditer(r'\d+', line)]
    numbers = [int(m) for m in re.findall(r'\d+', line)]

    for index, number in zip(number_indexes, numbers):
        if is_previous_line_exists(line_number) and is_adjacent(index, number, lines[line_number - 1]):
            sum += number

        if is_adjacent(index, number, lines[line_number]):
            sum += number

        if is_next_line_exists(line_number, lines) and is_adjacent(index, number, lines[line_number + 1]):
            sum += number

    return sum

def is_adjacent(index: int, number: int, line: str) -> bool:
    symbol_indexes = [m.start() for m in re.finditer(r'\*|\$|@|\+|=|#|\/|&|%|\^|\-', line)]   

    for symbol_index in symbol_indexes:
        if symbol_index >= index - 1 and symbol_index <= index + len(str(number)):
            return True

    return False

def is_previous_line_exists(current_line_number: int) -> bool:
    return current_line_number > 0

def is_next_line_exists(current_line_number: int, lines: list) -> bool:
    return current_line_number < len(lines) - 1