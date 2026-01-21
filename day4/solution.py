import sys
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view


def calcRemove(num_data):
    padded_matrix = np.pad(num_data, pad_width=1, mode="constant", constant_values=0)

    windows = sliding_window_view(padded_matrix, (3, 3))
    result = 0
    for (i, j), value in np.ndenumerate(num_data):
        if value == 1 and windows[i][j].sum() < 5:
            result += 1
            num_data[i][j] = 0

    if result == 0:
        return result
    else:
        return result + calcRemove(num_data)


def solve(part=1, filename="input.txt"):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            data = [list(line.strip("\n")) for line in lines]
            grid = np.array(data)
            num_data = np.where(grid == "@", 1, 0)

            print(calcRemove(num_data))

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return


if __name__ == "__main__":
    part = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    filename = sys.argv[2] if len(sys.argv) > 2 else "input.txt"
    solve(part, filename)