import pytest
import sys

from pathlib import Path

import advent_2025.solutions.day1 as d

class TestConvertDirections():
    def test_left(self):
        x = d.convert_directions(['L1'])
        assert x == [-1]
    
    def test_right(self):
        x = d.convert_directions(['R9'])
        assert x == [9]

    def test_multiple(self):
        x = d.convert_directions(['L2', 'R8', 'L99'])
        assert x == [-2, 8, -99]

class TestSimplifyInputCode():
    def test_simple_right(self):
        code, turns = d.simplify_input_code(42)
        assert (code, turns) == (42, 0)

    def test_simple_left(self):
        code, turns = d.simplify_input_code(-10)
        assert(code, turns) == (-10, 0)

    def test_complex_right(self):
        code, turns = d.simplify_input_code(142)
        assert (code, turns) == (42, 1)

    def test_complex_left(self):
        code, turns = d.simplify_input_code(-310)
        assert(code, turns) == (-10, 3)

class TestTurnDial():
    def test_turn_right(self):
        x = d.turn_dial(2, 10)
        assert x == 12

    def test_turn_right_past_zero(self):
        x = d.turn_dial(99, 2)
        assert x == 1

    def test_turn_left(self):
        x = d.turn_dial(10, -2)
        assert x == 8

    def test_turn_left_past_zero(self):
        x = d.turn_dial(2, -4)
        assert x == 98
    
class TestComplete():
    def test_part_one(self):
        x = d.day_one(test=True, problem_part=1)
        assert x == 3

    def test_part_two(self):
        x = d.day_one(test=True, problem_part=2)
        assert x == 6