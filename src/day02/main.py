#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser('aoc2025 day02')
    parser.add_argument('-t', '--test', type=bool, default=False, action=argparse.BooleanOptionalAction, help='Testing input file')
    args = parser.parse_args()
    if args.test:
        input_file = 'src/day02/test_input.txt'
    else:
        input_file = 'src/day02/input.txt'
    with open(input_file, "r") as f:
        data = f.read().strip()
    
    part1 = 0
    part2 = 0
    for line in data.split(','):
        first_id,last_id = int(line.split('-')[0]), int(line.split('-')[1])
        
        for i in range (first_id, last_id+1):
            if len(str(i)) == 1:    # Skip single digit IDs
                continue



    print(part1)
    print(part2)

    with open('src/day02/output.txt', 'w') as f:
        f.write(f"{part1}\n")
        f.write(f"{part2}\n")

if __name__ == "__main__":
    main()
