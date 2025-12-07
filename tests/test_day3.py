import pytest
import sys

from pathlib import Path

import advent_2025.solutions.day3 as d


class TestSolveBattery:
    def test_simple_2_digit_one(self):
        x = d.solve_battery(987654321111111, 2)
        assert x == 98

    def test_simple_2_digit_two(self):
        x = d.solve_battery(811111111111119, 2)
        assert x == 89

    def test_simple_2_digit_three(self):
        x = d.solve_battery(234234234234278, 2)
        assert x == 78

    def test_simple_2_digit_four(self):
        x = d.solve_battery(818181911112111, 2)
        assert x == 92


class TestFullSolution:
    def test_part_one(self):
        x = d.solve_day_three(digits=2, test=True)
        assert x == 357

    def test_part_two(self):
        x = d.solve_day_three(digits=12, test=True)
        assert x == 3121910778619
