import pytest
import sys
import numpy as np

from pathlib import Path

import advent_2025.solutions.day4 as d


class TestSumAdjacentArray:
    def test_1d_array(self):
        x = np.array([[1, 2], [3, 4]])
        expect = np.array([[9, 8], [7, 6]])
        assert np.array_equal(d.sum_adjacent_2d(x), expect)


class TestGetThresholdMatrix:
    def test_get_threshold_matrix(self):
        x = np.array([[1, 2], [3, 4]])
        expect = np.array([[1, 1], [1, 0]])
        assert np.array_equal(d.get_threshold_matrix(arr=x, threshold=4), expect)


class TestGetSumThrsholdMatrix:
    def test_get_threshold_matrices(self):
        x = np.array([[1, 2], [3, 4]])
        expect = np.array([[0, 0], [1, 1]]), np.array([[1, 1], [0, 0]])
        assert np.array_equal(d.get_threshold_matrices(arr=x, threshold=8), expect)


class TestFull:
    def test_full_demo_data(self):
        x = d.day_four_part_one(test=True)
        assert x == 13

    def test_full_demo_part_two(self):
        x = d.day_four_part_two(test=True)
        assert x == 43
