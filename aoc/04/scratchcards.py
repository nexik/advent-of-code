from .card import Card
from pprint import pprint

def part_one(lines: list) -> int:
    return sum(card.points() for card in get_cards(lines))

def part_two(lines: list) -> int:
    cards = get_cards(lines)

    instances = [1] * len(cards)
    pprint(len(instances))
    
    for index, card in enumerate(cards):
        for i in range(card.id, card.id + card.count_hits()):
            instances[i] += instances[index]

    return sum(instances)

def get_cards(lines: list) -> list[Card]:
    return [Card.from_string(line) for line in lines]