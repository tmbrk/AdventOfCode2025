import sys

def get_max_joltage(bank, k):
    # Filter non-digits just in case, though input seems clean
    bank = "".join(d for d in bank if d.isdigit())
    n = len(bank)
    if n < k:
        return 0
    
    current_idx = 0
    result = []
    
    for i in range(k):
        remaining_needed = k - i
        # We need to leave (remaining_needed - 1) digits after the one we pick.
        # So the last index we can pick is n - remaining_needed.
        # The slice end (exclusive) is n - remaining_needed + 1.
        search_end = n - remaining_needed + 1
        
        window = bank[current_idx : search_end]
        best_digit = max(window)
        
        # Find first occurrence of best_digit in the window
        relative_idx = window.index(best_digit)
        absolute_idx = current_idx + relative_idx
        
        result.append(best_digit)
        current_idx = absolute_idx + 1
        
    return int("".join(result))

def solve(part=1, filename='day3/input.txt'):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    k = 12 if part == 2 else 2
    
    total_joltage = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        max_j = get_max_joltage(line, k)
        total_joltage += max_j
        
    print(total_joltage)

if __name__ == '__main__':
    part = 1
    filename = 'day3/input.txt'
    if len(sys.argv) > 1:
        part = int(sys.argv[1])
    if len(sys.argv) > 2:
        filename = sys.argv[2]
    solve(part, filename)
