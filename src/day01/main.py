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
    for line in data.splitlines():
        r_times = 0
        l_times = 0
        if line.startswith('R'):
            r_turn = int(line.split('R')[1])
            position += r_turn
            if position > 100:
                if position % 100 == 0:
                    r_times = (position // 100) - 1
                else:
                    r_times = (position) // 100
                part2 += r_times
        elif line.startswith('L'):
            l_turn = int(line.split('L')[1])
            if position == 0:
                l_times = abs((position - l_turn) // 100) - 1
                part2 += l_times
            else:
                l_times = abs((position - l_turn) // 100)
                part2 += l_times
            position -= l_turn
        position = position % 100

        if position == 0:
            part1 += 1

    part2 += part1

    print(part1)
    print(part2)

    with open('src/day01/output.txt', 'w') as f:
        f.write(f"{part1}\n")
        f.write(f"{part2}\n")

if __name__ == "__main__":
    main()
