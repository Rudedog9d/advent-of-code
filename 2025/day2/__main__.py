from pathlib import Path

data = [
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9",
]
data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


def is_safe(a: int | None, b: int, c: int) -> bool:
    # b and c must have a change, and be within 3 of each other
    bc = b - c
    if 0 == bc:
        # no change, unsafe
        return False
    if not 0 < abs(bc) <= 3:
        # change greater than 3, unsafe
        return False

    # a is previous number, so a -> b as b -> c
    if a is not None:
        ab = a - b
        if (ab < 0 < bc) or (ab > 0 > bc):
            return False

    return True

def seq_is_safe(numbers: list[int]) -> bool:
    safe = True
    safe &= is_safe(None, *numbers[0:2])
    for i in range(2, len(numbers)):
        safe &= is_safe(*numbers[i - 2:i + 1])
        if not safe:
            return safe
    return safe


def part1():
    count = 0
    for line in data:
        numbers = list(map(int, line.split()))
        if seq_is_safe(numbers):
            count += 1

    return count


def part2():
    count = 0
    for line in data:
        numbers = list(map(int, line.split()))
        if seq_is_safe(numbers):
            count += 1
            continue

        # try cutting out numbers to make things safe
        for i in range(len(numbers)):
            if seq_is_safe(numbers[:i] + numbers[i + 1:]):
                count += 1
                break

    return count


print(f"part1: {part1()}")
print(f"part2: {part2()}")
