import sys
from pathlib import Path
from loguru import logger
from typing import Union
import numpy as np

MODULE_ROOT = Path(__file__).resolve().parent.parent
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def load_array(test=False) -> np.ndarray:
    """
    Load a text file containing rows of '@' and '.' characters into a NumPy array.

    Conversion:
        '@' -> 1
        '.' -> 0

    Args:
        path (Union[str, Path]): Path to the input text file.

    Returns:
        np.ndarray: A 2D NumPy array of integers (0s and 1s).

    Notes:
        - Lines are stripped of whitespace.
        - Empty lines are ignored.
    """
    if test == True:
        path = RAW_DATA_DIR / "test_day_4.txt"
    else:
        path = RAW_DATA_DIR / "day_4.txt"

    rows = []

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            row = []
            for ch in line:
                if ch == "@":
                    row.append(1)
                elif ch == ".":
                    row.append(0)
                else:
                    raise ValueError(f"Unexpected character '{ch}' in input file.")
            rows.append(row)

    return np.array(rows, dtype=int)


def sum_adjacent_2d(arr: np.ndarray) -> np.ndarray:
    """
    Compute the sum of adjacent neighbours for each element in a 2D NumPy array.

    For each cell in the array, this function sums the values of its neighbours:
    - If include_diagonals is False: only up, down, left, right neighbours are used.
    - If include_diagonals is True: diagonal neighbours are also included.

    The element itself is not included in the sum. Out-of-bounds neighbours are
    treated as zero via zero-padding at the array edges.

    Args:
        arr (np.ndarray): A 2D NumPy array of numeric values.

    Returns:
        np.ndarray: A 2D NumPy array of the same shape as `arr`, where each
        element is the sum of its neighbours as defined above.

    Raises:
        ValueError: If `arr` is not 2-dimensional.
    """
    if arr.ndim != 2:
        raise ValueError("Input array `arr` must be 2-dimensional.")

    # Pad with zeros around the border to make edge handling easier
    padded = np.pad(arr, pad_width=1, mode="constant", constant_values=0)

    # 8-directional neighbours: up, down, left, right
    neighbour_sum = (
        padded[:-2, 1:-1]  # up
        + padded[2:, 1:-1]  # down
        + padded[1:-1, :-2]  # left
        + padded[1:-1, 2:]  # right
        + padded[:-2, :-2]  # up-left
        + padded[:-2, 2:]  # up-right
        + padded[2:, :-2]  # down-left
        + padded[2:, 2:]  # down-right
    )

    return neighbour_sum


def get_threshold_matrix(arr: np.ndarray, threshold: int) -> np.ndarray:
    """From sum matrix, get positions below threshold"""
    return (arr < threshold).astype(int)


def get_stuck_matrix(arr: np.ndarray, threshold: int) -> np.ndarray:
    """From sum matrix, get positions at or above threshold"""
    return (arr >= threshold).astype(int)


def get_threshold_matrices(arr: np.ndarray, threshold: int) -> np.ndarray:
    """Calculate the neighbour sums and return 1 for each entry below threshold."""
    # Calculate the sum adjacent matrix
    sum_adj_matrix = sum_adjacent_2d(arr)

    # Calculate the threshold matrix
    sum_threshold_matrix = get_threshold_matrix(sum_adj_matrix, threshold)

    # Calculate the "stuck" matrix
    stuck_matrix = get_stuck_matrix(sum_adj_matrix, threshold)

    return sum_threshold_matrix, stuck_matrix


def calculate_sum_removable_entries(arr: np.ndarray, threshold: int) -> int:
    """Calculate the number of rolls to be removed and return the matrix after removal"""
    # Calculate the threshold matrix
    sum_threshold_matrix, stuck_matrix = get_threshold_matrices(arr, threshold)
    # Multiply element-wise by the original matrix
    prod_matrix = sum_threshold_matrix * arr
    # Calculate the sum
    rolls_accesible = prod_matrix.sum()
    # Calculate the new matrix
    new_matrix = arr * stuck_matrix

    return rolls_accesible, new_matrix


# Final Functions


def day_four_part_one(test=False):
    input = load_array(test)
    out, _ = calculate_sum_removable_entries(input, threshold=4)
    return out


def day_four_part_two(test=False):
    # Load Array
    current_matrix = load_array(test)
    rolls_removed = 0
    available_moves = 999  # Any large value to kick off the loop

    while available_moves > 0:
        available_moves, new_matrix = calculate_sum_removable_entries(current_matrix, threshold=4)
        rolls_removed += available_moves
        current_matrix = new_matrix

    return rolls_removed


if __name__ == "__main__":
    logger.success("Part One: {}".format(day_four_part_one()))
    logger.success("Part One: {}".format(day_four_part_two()))
