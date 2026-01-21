import sys
import re

from numpy.lib import _stride_tricks_impl


def parse_input(filename):
    with open(filename, 'r') as f:
        content = f.read()
    
    parts = content.split('\n\n')
    
    ranges_str = parts[0].strip().split('\n')
    numbers_str = parts[1].strip().split('\n') if len(parts) > 1 else []

    ranges = []
    for r_str in ranges_str:
        if r_str:
            start_str, end_str = r_str.split('-')
            ranges.append((int(start_str), int(end_str)))
            
    numbers = [int(n) for n in numbers_str if n]
            
    return ranges, numbers


def part1(data):
    result = []
    for prod in data[1]:
        for r in data[0]:
            if prod >= r[0] and prod <= r[1]:
                result.append(prod)
                break
    return len(result)


def reduce_fresh(fresh, result=[]):
    if not fresh:
        return result
    elif not result:
        return reduce_fresh(fresh, [fresh[0]])
    else:
        check = fresh.pop(0)
        if result[-1][1] >= check[0] and result[-1][1] <= check[1]:
            result[-1][1] = check[1]
        elif result[-1][1] < check[0]:
            result.append(check)
        return reduce_fresh(fresh, result)


def part2(data):
    data[0].sort(key=lambda x: x[0])
    result = reduce_fresh(data[0])
    out = 0
    for x in result:
        out += x[1] + 1 - x[0]

    return out


def solve(filename):
    ranges, numbers = parse_input(filename)

    p1 = part1(ranges)
    print(f"Part 1: {p1}")

    p2 = part2(numbers)
    print(f"Part 2: {p2}")


if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    solve(filename)
