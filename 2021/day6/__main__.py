from pathlib import Path

data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]
# data = ["3,4,3,1,2"]


def part1():
    fish = [int(x) for x in data[0].split(',')]
    target = 80
    for i in range(target):
        next = []
        for f in fish:
            if f == 0:
                next += [6, 8]
            else:
                next.append(f - 1)
        fish = next
    return len(fish)


def part2():
    fish = [0] * 9
    for f in [int(x) for x in data[0].split(',')]:
        fish[f] += 1
    for day in range(256):
        new = 0
        for i, n in enumerate(fish):
            if i == 0:
                new = n
            else:
                fish[i-1] = n
            fish[i] = 0
        fish[6] += new
        fish[8] = new
    return sum(fish)


print(f"part1: {part1()}")
print(f"part2: {part2()}")
