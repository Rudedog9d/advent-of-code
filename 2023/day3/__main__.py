import re
from pathlib import Path
from typing import Literal, Dict, List, Tuple

data = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
""".strip().splitlines()
# data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


def get_iter_neighbor(it: str | List, start: int, end: int) -> str | List:
    if start > 0:
        start -= 1
    if end < len(it):
        end += 1
    print('get_iter_neighbor', it, start, end)
    return it[start:end]


ANTI_SYMBOLS = ['.', *[str(i) for i in range(0, 9)]]


def check_p1_position(idx: int, start: int, end: int) -> bool:
    # check line with part
    line = data[idx]
    if start > 0 and line[start-1] not in ANTI_SYMBOLS:
        print('line start match')
        return True
    if end < len(line) - 1 and line[end+1] not in ANTI_SYMBOLS:
        print('line end match')
        return True

    if start > 0:
        start -= 1
    if end < len(line) - 1:
        end += 1

    if idx > 0:
        for i in range(start, end):
            if data[idx - 1][i] not in ANTI_SYMBOLS:
                return True

    if idx < len(data) - 1:
        for i in range(start, end):
            if data[idx + 1][i] not in ANTI_SYMBOLS:
                return True

    return False


def find_part_number(idx: int, line: str) -> List[str]:
    ret = []
    match = re.search('\d+', line)
    if not match:
        return ret
    start, end = match.regs[0]
    print(line, start, end, end=' ')
    if check_p1_position(idx, start, end - 1):
        ret.append(int(match.group()))
        print('match')
    else:
        print('no match!')
    ret.extend(find_part_number(idx, line[end:]))
    return ret


def part1():
    sum = 0
    for i, line in enumerate(data):
        for x in find_part_number(i, line):
            sum += int(x)

    return sum


def part2():
    return ''



print(f"part1: {part1()}")
print(f"part2: {part2()}")
