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
    """Read Data from Day 1 file into a list."""
    if test:
        file_path = RAW_DATA_DIR / "test_day_3.txt"
    else:
        file_path = RAW_DATA_DIR / "day_3.txt"
    return [line.strip() for line in file_path.read_text().splitlines()]


def solve_battery(n: int, k: int) -> list[int]:
    """
    Recursively extract k peak digits from integer n.

    At each step:
    - Consider the current string s of length m.
    - You may choose the next digit only from s[0 : m - k + 1]
      so that there are still k-1 digits available to the right.
    - Take the highest digit in that prefix as the next peak,
      then recurse to the right of its first occurrence for k-1 more digits.

    Parameters
    ----------
    n : int
        A positive integer from which to extract digits.
    k : int
        The number of digits to extract (1 <= k <= number of digits in n).
    """
    s = str(n)
    m = len(s)

    if k < 1 or k > m:
        raise ValueError("k must be between 1 and the number of digits in n.")

    def _helper(sub_s: str, remaining: int) -> list[int]:
        # Base case: only one digit to choose; take the maximum from what is left
        if remaining == 1:
            return [max(int(d) for d in sub_s)]

        m_sub = len(sub_s)
        # We can only search up to index (m_sub - remaining) inclusive
        # so slice end is (m_sub - remaining + 1)
        search_end = m_sub - remaining + 1
        prefix = sub_s[:search_end]

        max_digit_char = max(prefix)
        max_digit = int(max_digit_char)
        first_idx = prefix.index(max_digit_char)

        # Recurse on the substring to the right of this chosen digit
        return [max_digit] + _helper(sub_s[first_idx + 1 :], remaining - 1)

    output_list = _helper(s, k)

    return int("".join(str(d) for d in output_list))


def solve_battery_bank(battery_bank: list, digits) -> int:
    """Solve puzzle for a set battery bank."""
    total = 0
    for battery in battery_bank:
        total += solve_battery(battery, digits)
    return total


def solve_day_three(digits, test=False):
    """Solve day three puzzle"""
    data = load_data(test=test)
    result = solve_battery_bank(data, digits)
    return result


if __name__ == "__main__":

    logger.remove()  # remove default sink
    logger.add(sys.stderr, level=LOGGING_LEVEL)

    part_one = solve_day_three(digits=2)
    logger.success("Part One Solution: {}".format(part_one))

    part_two = solve_day_three(digits=12)
    logger.success("Part Two Solution: {}".format(part_two))
