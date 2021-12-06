import sys
import pandas as pd


def count_increase(input):
    input["prev_meas"] = input["meas"].shift(1)
    num_incr = sum(input["meas"] > input["prev_meas"])
    return num_incr


def count_window_increase(input):
    input["window"] = input["meas"].rolling(3).sum()
    input["prev_window"] = input["window"].shift(1)
    num_incr = sum(input["window"] > input["prev_window"])
    return num_incr


if __name__ == "__main__":

    filename = sys.argv[-1]
    input = pd.read_csv(filename, names=["meas"])

    # solve
    print("part 1:", count_increase(input))
    print("part 2:", count_window_increase(input))
