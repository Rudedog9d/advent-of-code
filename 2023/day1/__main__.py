import re
from pathlib import Path

data = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet",
]
data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


def part1():
    sum = 0
    for line in data:
        first = re.match('.*(\d+).*', line[::-1]).group(1)[::-1]
        last = re.match('.*(\d+).*', line).group(1)
        sum += int(first + last)
    return sum


numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def part2():
    sum = 0
    for line in data:
        first = re.match(f'.*(\d+|{"|".join([k[::-1] for k in numbers.keys()])}).*', line[::-1]).group(1)[::-1]
        last = re.match(f'.*(\d+|{"|".join(numbers.keys())}).*', line).group(1)
        if first in numbers:
            first = numbers[first]
        if last in numbers:
            last = numbers[last]
        sum += int(f'{first}{last}')
    return sum


print(f"part1: {part1()}")
print(f"part2: {part2()}")
