import unittest
import importlib

module = importlib.import_module('aoc.03.gear_rations')

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
