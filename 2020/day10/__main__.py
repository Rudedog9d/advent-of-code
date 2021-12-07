from pathlib import Path
from math import factorial, pow

data = [int(line.strip()) for line in open(Path(Path(__file__).parent, 'input.txt'))]


# # Sample Data
data = [
    28,
    33,
    18,
    42,
    31,
    14,
    46,
    20,
    48,
    47,
    24,
    23,
    49,
    45,
    19,
    38,
    39,
    11,
    1,
    32,
    25,
    35,
    8,
    17,
    7,
    9,
    4,
    2,
    34,
    10,
    3
]


# data = [
#     16,
#     10,
#     15,
#     5,
#     1,
#     11,
#     7,
#     19,
#     6,
#     12,
#     4,
# ]


data.sort()
# Insert charging outlet, which is always zero
data.insert(0, 0)
# Insert device, always 3 higher than last adapter
data.append(data[-1] + 3)


def part1():
    diff1 = 0
    diff3 = 0
    for i, x in enumerate(data):
        y = data[i-1]
        if x - y == 1:
            diff1 += 1
        elif x - y == 3:
            diff3 += 1
    print(f'diff1={diff1} diff3={diff3} part1 ans={diff1 * diff3}')


def part2(start=0):
    total = 1
    i = 0
    while i < len(data) - 1:
        x = data[i]
        paths = -1
        for z in (1, 2, 3):
            if x + z in data:
                i = data.index(x + z, i)
                # paths += 1
                paths += 1
                print(f'x={x} z={z} paths={paths} total={total}')
        # total *= factorial(paths)
        print(f'total *= {pow(2, paths)}')
        # total += pow(2, paths) - 1
        total *= pow(2, paths)
        # total += paths - 1
    print(f'part 2: total paths={total}')

part1()
part2()
