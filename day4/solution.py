import sys
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def my_function(val):
    return val.sum()


def solve(part=1, filename="input.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            data = [list(line.strip("\n")) for line in lines]
            grid = np.array(data)
            num_data = np.where(grid == "@", 1, 0)
            padded_matrix = np.pad(
                num_data, pad_width=1, mode="constant", constant_values=0
            )

            windows = sliding_window_view(padded_matrix, (3, 3))
            result = 0
            for (i, j), value in np.ndenumerate(num_data):
                if value == 1 and windows[i][j].sum() < 5:
                    result += 1

            print(result)

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return


if __name__ == "__main__":
    part = 1
    filename = "input.txt"
    part = int(sys.argv[1])
    filename = sys.argv[2]
    solve(part, filename)
