import sys

def solve(part=1, filename='day4/input.txt'):
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    # TODO: Implement solution
    print(f"Solving Part {part} with {len(lines)} lines of input.")

if __name__ == '__main__':
    part = 1
    filename = 'day4/input.txt'
    if len(sys.argv) > 1:
        part = int(sys.argv[1])
    if len(sys.argv) > 2:
        filename = sys.argv[2]
    solve(part, filename)
