from pathlib import Path

data = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".strip().splitlines()
data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


def part1():
    total = 0
    for line in data:
        card_pts = 0
        card, line = line.strip().split(':')
        winning, numbers = line.strip().split('|')
        winning = winning.strip().split(' ')
        for number in numbers.strip().split(' '):
            if not number:
                continue  # sometimes we parse empty strings from lines
            if number in winning:
                # print(f'{card}: "{number}" in {winning}')
                card_pts = (card_pts * 2) if card_pts else 1
        # print(card, card_pts)
        total += card_pts
    return total


def part2():
    result = [1 for _ in range(len(data))]
    for idx, line in enumerate(data):
        wins = 0
        card, line = line.strip().split(':')
        winning, numbers = line.strip().split('|')
        winning = winning.strip().split(' ')
        for number in numbers.strip().split(' '):
            if not number:
                continue  # sometimes we parse empty strings from lines
            if number not in winning:
                continue
            wins += 1

        for i in range(wins):
            if idx + i + 2 > len(data):
                print('skipping due to end of data')
                continue  # don't go past end of table
            result[idx + i + 1] += result[idx]

    return sum(result)


print(f"part1: {part1()}")
print(f"part2: {part2()}")
