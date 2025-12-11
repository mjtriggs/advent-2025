import pytest
import sys
import numpy as np

from pathlib import Path

import advent_2025.solutions.day5 as d


class TestLoadData:
    def test_load_data(self):
        expected_a = ["3-5", "10-14", "16-20", "12-18"]
        expected_b = [1, 5, 8, 11, 17, 32]
        assert expected_a, expected_b == d.load_data(test=True)


class TestCleaning:
    def test_range_cleaning(self):
        pass

    def test_get_ingredient_range(self):
        input = "1-3"
        expected = [1, 3]
        assert d.get_ingredient_range(input) == expected

    def test_get_ingredient_range_2(self):
        input = "1-2"
        expected = [1, 2]
        assert d.get_ingredient_range(input) == expected

    def test_get_ingredient_range_3(self):
        input = "0-8"
        expected = [0, 8]
        assert d.get_ingredient_range(input) == expected

    def test_fresh_ingredient_ranges(self):
        input = ["1-3", "3-5"]
        expected = [[1, 3], [3, 5]]
        assert d.get_fresh_ingredient_ranges(input) == expected

    def test_create_ingredient_ranges_2(self):
        input = ["1-3", "1-3"]
        expected = [[1, 3], [1, 3]]
        assert d.get_fresh_ingredient_ranges(input) == expected


class TestCheckLogic:
    def test_is_ingredient_valid(self):
        input = 4
        ranges = [[1, 10], [12, 15]]
        assert d.is_ingredient_valid(input, ranges)

    def test_is_ingredient_valid_2(self):
        input = 42
        ranges = [[1, 10], [12, 15]]
        assert not d.is_ingredient_valid(input, ranges)

    def test_simplify_ranges(self):
        input = [[1, 3], [2, 4], [8, 10]]
        output = [[1, 4], [8, 10]]
        assert d.simplify_ranges(input) == output


class TestCheckEndToEnd:
    def test_check_end_to_end_part_one(self):
        output, _ = d.day_five(True)
        assert output == 3

    def test_check_end_to_end_part_two(self):
        _, output = d.day_five(True)
        assert output == 14
