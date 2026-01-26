import sys

def solve_part1(content):
    lines = content.strip().split('\n')
    # TODO: Implement Part 1
    return 0

def solve_part2(content):
    lines = content.strip().split('\n')
    # TODO: Implement Part 2
    return 0

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    with open(filename, 'r') as f:
        content = f.read()
    
    print(f"Part 1: {solve_part1(content)}")
    print(f"Part 2: {solve_part2(content)}")
