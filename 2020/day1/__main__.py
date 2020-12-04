import time
from pathlib import Path


def part1(arr1, arr2):
    iteration = 0
    for n1 in arr1:
        for n2 in arr2:
            iteration += 1
            if n1 + n2 == 2020:
                print('iteration')
                return iteration, n1 * n2


def part2(arr1, arr2):
    iteration = 0
    for n1 in arr1:
        for n2 in arr2:
            for n3 in arr2:
                iteration += 1
                if n1 + n2 + n3 == 2020:
                    return iteration, n1 * n2 * n3


def sort_data(src, dst):
    with open(src) as f:
        data = [int(l) for l in f.readlines()]

    data.sort()
    with open(dst, 'w') as f:
        f.writelines(str(i) + '\n' for i in data)

    return data


input_file = Path(Path(__file__).parent, 'input.txt')
sorted_input_file = Path(Path(__file__).parent, 'input_sorted.txt')
if not sorted_input_file.is_file():
    print('sorting data and caching in {}'.format(input_file))
    data1 = sort_data(input_file, sorted_input_file)
else:
    print('using cached data from {}'.format(input_file))
    with open(Path(Path(__file__).parent, 'input_sorted.txt')) as f:
        data1 = [int(l) for l in f.readlines()]

data2 = data1.copy()
data2.reverse()
print("Part 1: {} ({} iterations)".format(*part1(data1, data2)))
print("Part 2: {} ({} iterations)".format(*part2(data1, data2)))
