
def is_invalid(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def solve():
    with open('day2/input.txt', 'r') as f:
        content = f.read().strip()
    
    ranges = content.split(',')
    total_sum = 0
    
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
    solve()
