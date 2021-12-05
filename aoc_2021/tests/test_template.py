# test template

import pytest
from aoc_2021.aoc_2021 import solve_template as aoc

def test_add_two_numbers():
    result = aoc.add_two(2, 3)
    assert result == 5
