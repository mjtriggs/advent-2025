import sys
from pathlib import Path
import pandas as pd
from loguru import logger
from typing import List

MODULE_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

LOGGING_LEVEL = "INFO"


def load_data(test=False):
    """Load data for day 2. Defaults for actuals but test data can be
    specified."""
    if test:
        path = PROJECT_ROOT / "data/raw/test_day_2.txt"
    else:
        path = PROJECT_ROOT / "data/raw/day_2.txt"

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    return [item.strip() for item in content.split(",")]


def get_start_end_id(code: str) -> tuple(int, int):
    """Split a text range into a start and end integer"""
    start, end = code.split("-")
    return int(start), int(end)


def get_candidate_values_for_range(code: str) -> list[int]:
    """For a text range, generate all numbers in the range (inclusive of start and end)"""
    start, end = get_start_end_id(code)
    return list(range(start, end + 1))


def get_full_candidate_list(input: list[str]) -> list[int]:
    """For a list of input ranges, generate the list of integers"""
    candidate_numbers = []
    for i in input:
        nums = get_candidate_values_for_range(i)
        candidate_numbers.extend(nums)
    return candidate_numbers


def is_invalid_id(id_value: int, problem_part: int) -> bool:
    """
    Determine whether an ID is invalid.

    An invalid ID is defined as a number whose decimal representation
    consists of some sequence of digits repeated exactly twice.
    Examples of invalid IDs include: 55 (5 repeated), 6464 (64 repeated),
    123123 (123 repeated).
    """
    s = str(id_value)

    if problem_part == 1:
        # Length must be even to be of the form XYXY
        if len(s) % 2 != 0:
            return False

        half = len(s) // 2
        first_half = s[:half]
        if first_half + first_half == s:
            return True
    elif problem_part == 2:
        # Single-digit IDs cannot be repeated patterns
        if len(s) < 2:
            return False

        doubled = s + s
        # A string composed of repeated substrings will always appear
        # as a proper substring of (s + s)[1:-1]
        return s in doubled[1:-1]

    return False


def get_invalid_ids_in_list(problem_part, nums: list[int]) -> list[int]:
    """From a list of integers, evaluate IDs and return a list of invalid IDs"""
    invalid_values = []
    for num in nums:
        if is_invalid_id(num, problem_part):
            invalid_values.append(num)

    if not invalid_values:
        invalid_values.append(0)

    return invalid_values


def solve_day_two(problem_part, test=False):
    """Overall solver for day two."""
    data = load_data(test)
    all_ids = get_full_candidate_list(data)
    invalid_ids = get_invalid_ids_in_list(problem_part=problem_part, nums=all_ids)
    out = sum(invalid_ids)
    return out


if __name__ == "__main__":

    logger.remove()  # remove default sink
    logger.add(sys.stderr, level=LOGGING_LEVEL)

    # Part 1
    logger.debug("Part I: Test")
    test_sol = solve_day_two(problem_part=1, test=True)
    logger.info("Part I: Test Solution - {}".format(test_sol))

    logger.debug("Part I: Actual")
    act_sol = solve_day_two(problem_part=1)
    logger.info("Part I: Actual Solution - {}".format(act_sol))

    # Part 2
    logger.debug("Part II: Test")
    test_sol = solve_day_two(test=True, problem_part=2)
    logger.info("Part II: Test Solution - {}".format(test_sol))

    logger.debug("Part II: Actual")
    act_sol = solve_day_two(problem_part=2)
    logger.info("Part II: Actual Solution - {}".format(act_sol))
