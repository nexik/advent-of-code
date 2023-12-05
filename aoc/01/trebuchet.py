from aoc.helpers import load_data_for_day

MAP_PART_ONE = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
MAP_PART_TWO = {**MAP_PART_ONE, **{"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}}

def part_one(lines: list) -> int:
    sum = 0
    
    for line in lines:
        line = line.strip()
        number = get_number(line, MAP_PART_ONE)
        sum += number
    
    return sum

def part_two(lines: list) -> int:
    sum = 0
    
    for line in lines:
        line = line.strip()
        number = get_number(line, MAP_PART_TWO)
        sum += number
    
    return sum

def get_number(line: str, map: dict) -> int:
    first_keys, first_values, last_keys, last_values = [], [], [], []

    for lookup_number in map:
        first_key = line.find(lookup_number)
        
        if first_key != -1:
            first_keys.append(first_key)
            first_values.append(map[lookup_number])

        last_key = line.rfind(lookup_number)

        if last_key != -1:
            last_keys.append(last_key)
            last_values.append(map[lookup_number])

    first = first_values[first_keys.index(min(first_keys))]
    last = last_values[last_keys.index(max(last_keys))]

    return (10 * first) + last