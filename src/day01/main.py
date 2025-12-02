#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser('aoc2025 day01')
    parser.add_argument('-t', '--test', type=bool, default=False, action=argparse.BooleanOptionalAction, help='Testing input file')
    args = parser.parse_args()
    if args.test:
        input_file = 'src/day01/test_input.txt'
    else:
        input_file = 'src/day01/input.txt'
    with open(input_file, "r") as f:
        data = f.read().strip()
    
    position = 50
    part1 = 0
    part2 = 0
    for i, line in enumerate(data.splitlines()):
        if line.startswith('R'):
            position += int(line.split('R')[1])
        elif line.startswith('L'):
            position -= int(line.split('L')[1])
        position = position % 100
        if position == 0:
            part1 += 1
    print(part1)

    with open('src/day01/output.txt', 'w') as f:
        f.write(f"{part1}\n")
        f.write(f"{part2}\n")

if __name__ == "__main__":
    main()
