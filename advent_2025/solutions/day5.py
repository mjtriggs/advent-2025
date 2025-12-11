import sys
from pathlib import Path
from loguru import logger
from typing import Union, List
from collections.abc import Iterable
import numpy as np
from tqdm import tqdm

MODULE_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_data(test=False) -> tuple[list[str], list[str]]:
    """
    Helper function to load either the test or real data.
    :param test: Description
    """
    if test:
        input_path = RAW_DATA_DIR / "test_day_5.txt"
    else:
        input_path = RAW_DATA_DIR / "day_5.txt"

    return load_split_file(input_path)


def load_split_file(filepath: str) -> tuple[list[str], list[str]]:
    """
    Load a text file and split it into two lists at the first blank line.

    Args:
        filepath (str): Path to the input text file.

    Returns:
        tuple[list[str], list[str]]:
            A tuple (section1, section2) where:
            - section1 contains all lines before the first blank line.
            - section2 contains all lines after the first blank line.
    """
    lines = Path(filepath).read_text().splitlines()

    section1 = []
    section2 = []

    blank_found = False

    for line in lines:
        if not blank_found:
            if line.strip() == "":
                blank_found = True
            else:
                section1.append(line)
        else:
            section2.append(line)

    return section1, section2


def get_ingredient_range(input_range: str) -> list[int]:
    """
    From a string representing a range of values, return a list containing all the integers of this range (inclusive).

    :param input_range: A range of ingredient values, expressed as a string.
    :type input_range: str
    :return: A list of the range.
    :rtype: list[int]
    """
    lower, upper = input_range.split("-")
    lower = int(lower)
    upper = int(upper)
    return [lower, upper]


def get_fresh_ingredient_ranges(input_ranges: list) -> list[list[int, int]]:
    ingredient_ranges = []
    for range in input_ranges:
        ingredient_ranges.append(get_ingredient_range(range))
    return ingredient_ranges


def is_ingredient_valid(ingredient: int, valid_ingredient_ranges: list[list[int, int]]) -> bool:
    for range in valid_ingredient_ranges:
        logger.debug("Ingredient: {}".format(ingredient))
        if (int(ingredient) >= range[0]) & (int(ingredient) <= range[1]):
            return True
    return False


def get_sum_valid_ingredients(ingredients: list[int], fresh_ingredients: set) -> list:
    valid_binary = []
    for ingredient in ingredients:
        if is_ingredient_valid(ingredient, fresh_ingredients):
            valid_binary.append(1)
        else:
            valid_binary.append(0)
    return sum(valid_binary)


def simplify_ranges(valid_ingredients: list[list[int, int]]) -> list[list[int, int]]:
    """
    Merge a collection of integer ranges into a list of non-overlapping ranges.

    Each input range is expected to be an iterable of exactly two integers
    [start, end]. The function will:
    - Sort all ranges by their start value.
    - Merge any ranges that overlap or touch.
      For example, [1, 4] and [3, 5] → [1, 5].

    Args:
        ranges (Iterable[Iterable[int]]): An iterable of [start, end] pairs.

    Returns:
        List[List[int]]: A list of merged, non-overlapping [start, end] ranges,
        sorted by start.
    """
    # Normalise to a sorted list of [start, end]
    sorted_ranges = sorted((int(s), int(e)) for s, e in valid_ingredients)

    if not sorted_ranges:
        return []

    merged: List[List[int]] = []
    current_start, current_end = sorted_ranges[0]

    for start, end in sorted_ranges[1:]:
        # If ranges overlap or touch (start <= current_end), merge them
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged.append([current_start, current_end])
            current_start, current_end = start, end

    # Append the final range
    merged.append([current_start, current_end])

    return merged


def get_total_numbers_in_range(range: list[list[int, int]]) -> int:
    simplified_range = simplify_ranges(range)
    return sum(b - a + 1 for a, b in simplified_range)


def day_five(test=False):
    # Load Data
    logger.info("Loading data range.")
    ranges, potential_ingredients = load_data(test)

    # Get valid ingredients list
    logger.info("Creating valid ingredients set.")
    valid_ingredients = get_fresh_ingredient_ranges(ranges)

    # Get sum of valid values
    logger.info("Checking valid values.")
    valid_sum = get_sum_valid_ingredients(potential_ingredients, valid_ingredients)

    # Get a the sum of range values
    logger.info("Getting range sum.")
    sum_ranges = get_total_numbers_in_range(valid_ingredients)

    return valid_sum, sum_ranges


if __name__ == "__main__":

    logger.remove()  # remove default sink
    # logger.add(sys.stderr, level="DEBUG")
    logger.add(sys.stderr, level="INFO")

    part_one, part_two = day_five()

    logger.success("Day Five - Part One: {}".format(part_one))
    logger.success("Day Five - Part Two: {}".format(part_two))
