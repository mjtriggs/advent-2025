import pytest
import sys

from pathlib import Path

import advent_2025.solutions.day2 as d


class TestDataPrep:
    def test_get_start_end_id(self):
        x = "123-456"
        a, b = d.get_start_end_id(x)
        assert (a, b) == (123, 456)

    def test_get_candidate_values_for_range(self):
        x = "123-125"
        assert d.get_candidate_values_for_range("123-125") == [123, 124, 125]

    def test_get_full_candidate_list(self):
        x = ["10-12", "20-21", "101-103"]
        out = d.get_full_candidate_list(x)
        expected_out = [10, 11, 12, 20, 21, 101, 102, 103]
        assert out == expected_out


class TestValidSingleIDsPartOne:
    def test_single_value_valid_one(self):
        input = "12"
        x = d.is_invalid_id(input, problem_part=1)
        assert x == False

    def test_single_value_valid_two(self):
        input = "12345"
        x = d.is_invalid_id(input, problem_part=1)
        assert x == False

    def test_single_value_invalid_one(self):
        input = "11"
        x = d.is_invalid_id(input, problem_part=1)
        assert x == True

    def test_single_value_invalid_two(self):
        input = "1212"
        x = d.is_invalid_id(input, problem_part=1)
        assert x == True


class TestInvalidIDListsPartOne:

    def test_range_all_valid(self):
        input = [999, 999, 1000]
        x = d.get_invalid_ids_in_list(nums=input, problem_part=1)
        assert x == [0]

    def test_range_invalid_one(self):
        input = [11, 12, 13, 20, 21, 22]
        x = d.get_invalid_ids_in_list(nums=input, problem_part=1)
        assert x == [11, 22]

    def test_range_invalid_two(self):
        # 998-1012
        input = [998, 999, 1000, 1001, 1010, 1011]
        x = d.get_invalid_ids_in_list(nums=input, problem_part=1)
        assert x == [1010]


class TestInvalidIDRangesPartOne:
    def test_range_example_one(self):
        input = "11-22"
        x = d.get_candidate_values_for_range(input)
        out = d.get_invalid_ids_in_list(nums=x, problem_part=1)
        assert out == [11, 22]

    def test_range_example_two(self):
        input = "38593856-38593862"
        x = d.get_candidate_values_for_range(input)
        out = d.get_invalid_ids_in_list(nums=x, problem_part=1)
        assert out == [38593859]

    def test_range_all_valid(self):
        input = "2121212118-2121212124"
        x = d.get_candidate_values_for_range(input)
        out = d.get_invalid_ids_in_list(nums=x, problem_part=1)
        assert out == [0]


class TestValidSingleIDsPartTwo:
    def test_single_value_valid_one(self):
        input = "12"
        x = d.is_invalid_id(input, problem_part=2)
        assert x == False

    def test_single_value_valid_two(self):
        input = "12345"
        x = d.is_invalid_id(input, problem_part=2)
        assert x == False

    def test_single_value_invalid_one(self):
        input = "123123123"
        x = d.is_invalid_id(input, problem_part=2)
        assert x == True

    def test_single_value_invalid_two(self):
        input = "11111111"
        x = d.is_invalid_id(input, problem_part=2)
        assert x == True

    def test_single_value_invalid_three(self):
        input = "123123123"
        x = d.is_invalid_id(input, problem_part=2)
        assert x == True

    def test_single_value_invalid_four(self):
        input = "2121212121"
        x = d.is_invalid_id(input, problem_part=2)
        assert x == True


class TestInvalidIDListsPartTwo:

    def test_range_new_invalid(self):
        input = [998, 999, 1000]
        x = d.get_invalid_ids_in_list(nums=input, problem_part=2)
        assert x == [999]

    def test_range_invalid_one(self):
        input = [11, 12, 13, 20, 21, 22]
        x = d.get_invalid_ids_in_list(nums=input, problem_part=2)
        assert x == [11, 22]

    def test_range_invalid_two(self):
        # 998-1012
        input = [998, 999, 1000, 1001, 1010, 1011]
        x = d.get_invalid_ids_in_list(nums=input, problem_part=2)
        assert x == [999, 1010]


class TestInvalidIDRangesPartTwo:
    def test_range_example_one(self):
        input = "11-22"
        x = d.get_candidate_values_for_range(input)
        out = d.get_invalid_ids_in_list(nums=x, problem_part=2)
        assert out == [11, 22]

    def test_range_example_two(self):
        input = "998-1012"
        x = d.get_candidate_values_for_range(input)
        out = d.get_invalid_ids_in_list(nums=x, problem_part=2)
        assert out == [999, 1010]

    def test_range_example_three(self):
        input = "2121212118-2121212124"
        x = d.get_candidate_values_for_range(input)
        out = d.get_invalid_ids_in_list(nums=x, problem_part=2)
        assert out == [2121212121]


class TestExample:
    def test_full_example_part_one(self):
        x = d.solve_day_two(problem_part=1, test=True)
        assert x == 1227775554

    def test_full_example_part_one(self):
        x = d.solve_day_two(problem_part=2, test=True)
        assert x == 4174379265
