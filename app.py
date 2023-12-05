from aoc.helpers import load_data_for_day 
import sys
import importlib

MODULE_NAMES = {
    "01" : 'aoc.01.trebuchet',
    "02" : 'aoc.02.cube_conundrum',
    "03" : 'aoc.03.gear_rations',
    "04" : 'aoc.04.scratchcards',
}

if __name__ == "__main__":
    day = sys.argv[1]
    module = importlib.import_module(MODULE_NAMES[day])
    print(f"Day: {day}")
    print(f"Part One result: {module.part_one(load_data_for_day('04'))}")
    print(f"Part Two result: {module.part_two(load_data_for_day('04'))}")
   