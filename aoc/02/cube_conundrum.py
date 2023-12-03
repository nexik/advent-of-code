from aoc.helpers import load_data_for_day
import re

def part_one() -> int:
    sum = 0

    for line in load_data_for_day('02'):
        if is_possible(line):
            sum += get_game_number(line)

    return sum

def part_two() -> int:
    sum = 0

    for line in load_data_for_day('02'):
        sum += get_max_cubes(line, 'red') * get_max_cubes(line, 'blue') * get_max_cubes(line, 'green')

    return sum

def get_game_number(line: str) -> int:
    return int(re.search('Game (\d+)', line).group(1))

def get_max_cubes(line: str, color: str) -> int:
    return max(map(int, re.findall('(\d+) ' + color, line)))

def is_possible(line: str) -> bool:   
    ALL = {'red': 12, 'green': 13, 'blue': 14} 
    reds = get_max_cubes(line, 'red')
    blues = get_max_cubes(line, 'blue')
    greens = get_max_cubes(line, 'green')
    
    return reds <= ALL['red'] and blues <= ALL['blue'] and greens <= ALL['green']