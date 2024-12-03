from pathlib import Path

data = [
    "3   4",
    "4   3",
    "2   5",
    "1   3",
    "3   9",
    "3   3",
]
data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


def get_lists() -> tuple[list[int], list[int]]:
    left = []
    right = []
    for line in data:
        a, b = map(int, line.split())
        left.append(a)
        right.append(b)
    return left, right


def part1():
    diff = 0
    left, right = get_lists()

    # pop lowest number from lists
    while len(left) > 0:
        a = left.pop(left.index(min(left)))
        b = right.pop(right.index(min(right)))
        diff += max(a, b) - min(a, b)
    return diff

def part2():
    left, right = get_lists()
    similarity = 0
    for a in left:
        # get count of a in right
        similarity += a * right.count(a)
    return similarity


print(f"part1: {part1()}")
print(f"part2: {part2()}")
