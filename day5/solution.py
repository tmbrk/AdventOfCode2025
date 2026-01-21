import sys
import re

from numpy.lib import _stride_tricks_impl


def parse_input(filename):
    fresh = []
    prods = []
    with open(filename, "r") as f:
        for line in f:
            if "-" in line:
                fresh.append(list(map(int, line.strip().split("-"))))
            elif "\n" == line:
                continue
            else:
                prods.append(int(line.strip()))

    return (fresh, prods)


def part1(data):
    result = []
    for prod in data[1]:
        for r in data[0]:
            if prod >= r[0] and prod <= r[1]:
                result.append(prod)
                break
    return len(result)


def part2(data):
    # TODO: Implement Part 2
    return None


def solve(filename):
    data = parse_input(filename)
    print(data)

    p1 = part1(data)
    print(f"Part 1: {p1}")

    p2 = part2(data)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    solve(filename)
