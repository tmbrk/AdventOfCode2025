
import sys

def is_invalid_part1(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def is_invalid_part2(n):
    s = str(n)
    length = len(s)
    # Check all possible substring lengths that could form the pattern
    for sub_len in range(1, length // 2 + 1):
        if length % sub_len == 0:
            substring = s[:sub_len]
            if substring * (length // sub_len) == s:
                return True
    return False

def solve(part=2):
    with open('day2/input.txt', 'r') as f:
        content = f.read().strip()
    
    ranges = content.split(',')
    total_sum = 0
    
    is_invalid = is_invalid_part2 if part == 2 else is_invalid_part1

    for r in ranges:
        if not r:
            continue
        start_str, end_str = r.split('-')
        start = int(start_str)
        end = int(end_str)
        
        for num in range(start, end + 1):
            if is_invalid(num):
                total_sum += num
                
    print(total_sum)

if __name__ == '__main__':
    part = 2
    if len(sys.argv) > 1:
        part = int(sys.argv[1])
    solve(part)
