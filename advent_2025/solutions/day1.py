# Day 1

import sys
from pathlib import Path
import pandas as pd
from loguru import logger
from typing import List

MODULE_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

STARTING_VALUE = 50

LOGGING_LEVEL = "INFO"

# Update the project path to reference other files 
sys.path.append(PROJECT_ROOT)


def read_data(test=False):
    """Read Data from Day 1 file into a list."""
    if test:
        file_path = RAW_DATA_DIR / 'test_day_1.txt'
    else:
        file_path = RAW_DATA_DIR / 'day_1.txt'
    return [line.strip() for line in file_path.read_text().splitlines()]



def convert_directions(values: List[str]) -> List[int]:
    """
    Convert a list of direction-coded strings into signed integers.

    Each value is expected to start with either 'R' or 'L' followed by digits.
    'R' values are treated as positive numbers (the 'R' is removed).
    'L' values are treated as negative numbers (the 'L' is removed and the
    sign inverted).
    """
    output = []

    for item in values:
        item = item.strip()

        if not item:
            raise ValueError("Empty string encountered in input list.")

        direction = item[0]
        number_str = item[1:]

        if direction not in {"R", "L"}:
            raise ValueError(f"Invalid prefix '{direction}' in '{item}'. Expected 'R' or 'L'.")

        if not number_str.isdigit():
            raise ValueError(f"Invalid numeric value in '{item}'.")

        number = int(number_str)

        if direction == "L":
            number = -number

        output.append(number)

    return output

def load_data(test=False):
    """Load and clean data for Day 1"""
    input_codes = read_data(test)
    clean_codes = convert_directions(input_codes)
    return clean_codes

def simplify_input_code(code):
    """Take a long input code and return the number of full and partial 
    rotations"""
    full_turns = abs(code) // 100
    sign = lambda x: -1 if x < 0 else 1
    new_code = sign(code) * (abs(code) % 100)
    return new_code, full_turns

def turn_dial(start_number, movement):
    """Take the starting number 'move the dial' by an appropriate amount, using
    modular arithmetic if required."""
    return (start_number + movement) % 100

def calculate_solution(codes, starting_value, problem_part):
    """Starting with a particular value, rotate the dial left and right
    according to the codes. Should an intermediate value land on zero,
    increment the count. Return the total number of zeroes at the end."""
    
    logger.debug("Starting solution calculation.")
    current_value = starting_value
    n_zeroes = 0
    
    if problem_part==1:
        for code in codes:
            current_value = turn_dial(current_value, code)
            if current_value == 0:
                n_zeroes += 1
    elif problem_part==2:
        for code in codes:

            # Count the number of full turns required
            logger.debug("Code Value: {}".format(code))
            new_code, full_turns = simplify_input_code(code)
            logger.debug("New input code: {}".format(new_code))
            n_zeroes += full_turns
            logger.debug("Number of Full Turns: {}".format(full_turns))

            if full_turns > 0:
                logger.debug("Increasing Count. New Count: {}".format(n_zeroes))

            logger.debug("Current Value: {}".format(current_value))
            logger.debug("Dial Value: {}".format(new_code))
            logger.debug("Sum: {}".format(new_code+current_value))
            
            if current_value == 0:
                pass
            elif (current_value + new_code >= 100) | (current_value + new_code <= 0):
                n_zeroes += 1
                logger.debug("Increasing Count. New Count: {}".format(n_zeroes))
            current_value = turn_dial(current_value, new_code)
            logger.debug("New current value: {}".format(current_value))
    return n_zeroes

def day_one(problem_part, test=False):
    
    # Load Data
    logger.debug("Loading input data.")
    codes = load_data(test)
    input_length = len(codes)
    logger.debug("Code Length: {}".format(input_length))

    # Calculate Solution
    solution = calculate_solution(problem_part=problem_part, 
                                  codes=codes,
                                  starting_value = STARTING_VALUE)

    # Return Answer
    return solution


if __name__ == "__main__":

    logger.remove()  # remove default sink
    logger.add(sys.stderr, level=LOGGING_LEVEL)

    # Part 1
    logger.debug("Part I: Test")
    test_sol = day_one(test=True, problem_part=1)
    logger.info("Part I: Test Solution - {}".format(test_sol))

    logger.debug("Part I: Actual")
    act_sol = day_one(problem_part=1)
    logger.info("Part I: Actual Solution - {}".format(act_sol))

    # Part 2
    logger.debug("Part II: Test")
    test_sol = day_one(test=True, problem_part=2)
    logger.info("Part II: Test Solution - {}".format(test_sol))

    logger.debug("Part II: Actual")
    act_sol = day_one(problem_part=2)
    logger.info("Part II: Actual Solution - {}".format(act_sol))