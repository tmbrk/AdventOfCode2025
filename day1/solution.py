def solve():
    # We'll use absolute position to make the math easier for Part 2
    # The dial is pos % 100
    current_pos = 50
    part1_count = 0
    part2_count = 0
    
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            direction = line[0]
            amount = int(line[1:])
            
            if direction == 'R':
                # Part 2: Number of multiples of 100 in (current_pos, current_pos + amount]
                # Formula: floor(B/100) - floor(A/100)
                A = current_pos
                B = current_pos + amount
                part2_count += (B // 100) - (A // 100)
                current_pos = B
            elif direction == 'L':
                # Part 2: Number of multiples of 100 in [current_pos - amount, current_pos)
                # Formula: floor((B-1)/100) - floor((A-1)/100)
                B = current_pos
                A = current_pos - amount
                part2_count += ((B - 1) // 100) - ((A - 1) // 100)
                current_pos = A
            
            # Part 1: Count if the dial ends exactly at 0
            if current_pos % 100 == 0:
                part1_count += 1
                
    print(f"Part 1: {part1_count}")
    print(f"Part 2: {part2_count}")

if __name__ == "__main__":
    solve()