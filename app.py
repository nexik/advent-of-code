import sys
import importlib

MODULE_NAMES = {
    "01" : 'aoc.01.trebuchet',
    "02" : 'aoc.02.cube_conundrum',
}

if __name__ == "__main__":
    day = sys.argv[1]
    module = importlib.import_module(MODULE_NAMES[day])
    print(f"Day: {day}")
    print(f"Part One result: {module.part_one()}")
    print(f"Part Two result: {module.part_two()}")
   