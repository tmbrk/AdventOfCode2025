import sys

def parse_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def part1(data):
    # TODO: Implement Part 1
    return None

def part2(data):
    # TODO: Implement Part 2
    return None

def solve(filename):
    data = parse_input(filename)
    
    p1 = part1(data)
    print(f"Part 1: {p1}")
    
    p2 = part2(data)
    print(f"Part 2: {p2}")

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    solve(filename)
