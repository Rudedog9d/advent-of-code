from pathlib import Path

data = open(Path(Path(__file__).parent, 'input.txt')).read()
# data = """
# 1000
# 2000
# 3000
#
# 4000
#
# 5000
# 6000
#
# 7000
# 8000
# 9000
#
# 10000
# """


def get_snack_totals():
    elves = []
    for elf in data.split('\n\n'):
        calories = 0
        for snack in elf.split():
            calories += int(snack)
        elves.append(calories)
    return elves


def part1():
    return max(get_snack_totals())


def part2():
    elves = get_snack_totals()
    elves.sort()
    return sum(elves[-3:])


print(f"part1: {part1()}")
print(f"part2: {part2()}")
