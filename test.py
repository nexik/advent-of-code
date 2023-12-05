import unittest
import importlib

module = importlib.import_module('aoc.03.gear_rations')

class TestScratchCards(unittest.TestCase):
    def setUp(self) -> None:
        self.module = importlib.import_module('aoc.04.scratchcards')

    def test_from_string(self) -> None:
        card = self.module.Card.from_string('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
        self.assertEqual(card.id, 1)
        self.assertEqual(card.winners, [41, 48, 83, 86, 17])
        self.assertEqual(card.draws, [83, 86, 6, 31, 17, 9, 48, 53])

    def test_points(self) -> None:
        card = self.module.Card.from_string('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53')
        self.assertEqual(card.points(), 8)

    def test_part_one(self) -> None:
        lines = [
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
        ]
        self.assertEqual(self.module.part_one(lines), 13)

    def test_part_two(self) -> None:
        lines = [
            'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
            'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
            'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
            'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
            'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
            'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
        ]
        self.assertEqual(self.module.part_two(lines), 30)

class TestDoubleGearRations(unittest.TestCase):
    def test_basic(self) -> None:
        result = module.calculate_sum_of_asterisk_gear_ratios([
            '11*11'
        ])
        self.assertEqual(result, 121)

    def test_none(self) -> None:
        result = module.calculate_sum_of_asterisk_gear_ratios([
            '11*.11'
        ])
        self.assertEqual(result, 0)
    
    def test_on_second_line(self) -> None:
        result = module.calculate_sum_of_asterisk_gear_ratios([
            '11...',
            '..*..',
            '...11'
        ])
        self.assertEqual(result, 121)

    def test_below_and_above(self) -> None:
        result = module.calculate_sum_of_asterisk_gear_ratios([
            '11.',
            '.*.',
            '.11',
        ])
        self.assertEqual(result, 121)

class TestNumberGearRations(unittest.TestCase):
    def test_467(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '467..114..',
            '...*......'
        ])
        self.assertEqual(result, 467)

    def test_thrid_line(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '........',
            '.24..4..',
            '......*.'
        ])
        self.assertEqual(result, 4)

    def test_dolar_sign(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11....11',
            '..$..$..',
            '11....11'
        ])
        self.assertEqual(result, 44)

    def test_dolar_on_first_and_last_line(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '$......$',
            '.1....1.',
            '.1....1.',
            '$......$'
        ])
        self.assertEqual(result, 4)

    def test_on_the_same_line(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '$11',
            '...',
            '11$',
            '...',
        ])
        self.assertEqual(result, 22)

    def test_eight_lines(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '$..',
            '.11',
            '.11',
            '$..',
            '..$',
            '11.',
            '11.',
            '..$'
        ])
        self.assertEqual(result, 44)

    def test_zero(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11.$.'
        ])
        self.assertEqual(result, 0)

    def test_at_symbol(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11@11'
        ])
        self.assertEqual(result, 22)

    def test_minus_sign(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11-11'
        ])
        self.assertEqual(result, 22)

    def test_plus_sign(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11+11'
        ])
        self.assertEqual(result, 22)

    def test_equals_sign(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11=11'
        ])
        self.assertEqual(result, 22)

    def test_hash_sign(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11#11'
        ])
        self.assertEqual(result, 22)

    def test_divide_sign(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11/11'
        ])
        self.assertEqual(result, 22)
    
    def test_ampersand_sign(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11&11'
        ])
        self.assertEqual(result, 22)

    def test_percent_sign(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11%11'
        ])
        self.assertEqual(result, 22)

    def test_power_sign(self) -> None:
        result = module.calculate_sum_of_gear_ratios([
            '11^11'
        ])
        self.assertEqual(result, 22)

if __name__ == '__main__':
    unittest.main()
