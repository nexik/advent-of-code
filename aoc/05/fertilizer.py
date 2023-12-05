from pprint import pprint
from itertools import groupby
import numpy as np
from tqdm import trange

def part_one(lines: list) -> int:
    seeds, maps = parse_input(lines)
    result = []
    for seed in seeds:
        for map in maps:
            seed = resolve_map(map, seed)
        result.append(seed)

    return np.min(result)

def part_two(lines: list) -> int:
    seeds, maps = parse_input(lines)
    maps.reverse()

    for i in trange(0, 100000000, 1000):
        seed = i
        
        for map in maps:
            seed = resolve_map_reverse(map, seed)
        
        for seeed, rang in np.array(seeds).reshape((-1, 2)):
            if seed >= seeed and seed < seeed + rang:
                iter_1 = i
                print(f"Part 2: {i} iteration 1")
                break
        else: 
            continue
        
        break

    for i in trange(iter_1 - 1000, iter_1 + 1):
        seed = i
        for map in maps:
            seed = resolve_map_reverse(map, seed)
        for seeed, rang in np.array(seeds).reshape((-1, 2)):
            if seed >= seeed and seed < seeed + rang:
                return i
        else: 
            continue
        

    return 0

def resolve_map(map: list, seed: int) -> int:
    for entry in map:
        if seed >= entry[1] and seed < (entry[1] + entry[2]):
            return seed - entry[1] + entry[0]
    
    return seed

def resolve_map_reverse(map: list, seed: int):
    for entry in map:
        if seed >= entry[0] and seed < (entry[0] + entry[2]):
            return seed - entry[0] + entry[1]
    return seed

def parse_input(lines: list):
    lines = [line for line in lines if line != ""]
    seeds = [int(s) for s in lines[0].split()[1:]]
    maps = []

    for line in lines[1:]:
        if 'map' in line:
            maps.append([])
        elif line != '':
            maps[-1].append([int(n) for n in line.split()])
    
    return seeds, maps
    