from day_01 import count_increase, count_window_increase
import pandas as pd

test_file = pd.read_csv("test_day_01.txt", names=["meas"])


def test_count_increase():
    assert count_increase(test_file) == 7


def test_count_window_increase():
    assert count_window_increase(test_file) == 5
