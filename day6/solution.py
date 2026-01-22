import operator
import sys
from functools import reduce
from itertools import groupby

import numpy as np

ops = {"*": operator.mul, "+": operator.add, "-": operator.sub, "/": operator.truediv}


def parse_input_part1(filename):
    return np.genfromtxt(filename, dtype=str)


def parse_input_part2(filename):
    with open(filename, "r") as file:
        lines = [list(line.strip("\n")) for line in file]
    return np.array(lines)


def part1(data):
    sums = data[:-1, :].T.astype(int)
    opps = data[-1, :]

    results = [reduce(ops[op], row) for row, op in zip(sums, opps)]
    return sum(results)


def part2(data):
    print(data)
    opps = data.T[:, -1]
    sims2 = data.T[:, :-1]
    print(sims2)
    sums = ["".join(x).strip() for x in list(sims2)]
    split_list = [list(group) for k, group in groupby(sums, lambda x: x == "") if not k]
    filteredopps = [str(x) for x in opps if x != " "]

    results = [
        reduce(ops[op], map(int, row)) for row, op in zip(split_list, filteredopps)
    ]

    return sum(results)


def solve(filename):
    data1 = parse_input_part1(filename)
    data2 = parse_input_part2(filename)

    p1 = part1(data1)
    print(f"Part 1: {p1}")

    p2 = part2(data2)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    solve(filename)
