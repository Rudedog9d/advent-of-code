import re
from pathlib import Path

# DATA = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
DATA = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
DATA = ''.join(line.strip() for line in open(Path(Path(__file__).parent, 'input.txt')))



def part1(data):
    total = 0
    match = re.search(r"mul\((\d+),(\d+)\)", data)
    while match:
        a, b = map(int, match.groups())
        total += a * b
        data = data[match.end():]
        match = re.search(r"mul\((\d+),(\d+)\)", data)
    return total


def part2(data):
    total = 0
    enabled = True
    mul = re.search(r"mul\((\d+),(\d+)\)", data)
    while mul:
        dont = re.search(r"don't\(\)", data)
        do = re.search(r"do\(\)", data)

        if dont and dont.start() < mul.start():
            enabled = False
        elif do and do.start() < mul.start():
            enabled = True

        if enabled:
            a, b = map(int, mul.groups())
            total += a * b


        data = data[mul.end():]
        mul = re.search(r"mul\((\d+),(\d+)\)", data)

        # only toggle if next do/don't is before the next mul
        if dont and mul and dont.start() < mul.start():
            enabled = False
        if do and mul and do.start() < mul.start():
            enabled = True
    return total


print(f"part1: {part1(DATA)}")
print(f"part2: {part2(DATA)}")
