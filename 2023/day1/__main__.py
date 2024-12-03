import re
# from collections.abc import dict_keys
from pathlib import Path
from typing import List, Iterable

data = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]
# data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]



def reverse_string(string: str) -> str:
    return string[::-1]


def part1():
    sum = 0
    return sum
    for line in data:
        first = re.match('[^\d]*(\d)', line).group(1)
        last = re.match('[^\d]*(\d)', reverse_string(line)).group(1)
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

def get_pattern(keys: Iterable[str]):
    str_digits = "|".join(keys)
    return f'[^\d|{str_digits}]*(\d|{str_digits})'


def part2():
    sum = 0
    print(get_pattern(numbers.keys()))
    print(get_pattern([reverse_string(x) for x in numbers.keys()]))
    for line in data:
        try:
            first = re.match(get_pattern(numbers.keys()), line).group(1)
            rev_pattern = get_pattern([reverse_string(x) for x in numbers.keys()])
            print(rev_pattern, reverse_string(line))
            m = re.match(rev_pattern, reverse_string(line))
            last = m.group(1)
            last = reverse_string(last)
        except:
            print('no match', line)
            raise

        if first in numbers:
            first = numbers[first]
        if last in numbers:
            last = numbers[last]

        print(first, last)
        sum += int(f'{first}{last}')
    return sum


print(f"part1: {part1()}")
print(f"part2: {part2()}")
