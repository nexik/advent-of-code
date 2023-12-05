import re

class Card:
    @classmethod
    def from_string(cls, line: str) -> 'Card':
        pattern = re.compile(r"Card\s+(\d+): ([\d\s]+?) \| ([\d\s]+)$")
        id, winners, draws = pattern.match(line).groups()
        
        return Card(int(id), [int(winner) for winner in winners.split()], [int(draw) for draw in draws.split()])
    
    def __init__(self, id: int, winners: list[int], draws: list[int]) -> None:
        self.id = id
        self.winners = winners
        self.draws = draws
    
    def points(self) -> int:
        count = self.count_hits()

        return 2 ** (count - 1) if count > 0 else 0
    
    def count_hits(self) -> int:
        return len([number for number in self.draws if number in self.winners])
    