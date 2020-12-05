from pathlib import Path

data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


def calc_row(s):
    top = 127
    bot = 0
    for c in s:
        if c == 'F':
            top = bot + int(((top - bot) / 2))
        elif c == 'B':
            bot = bot + int(((top - bot) / 2)) + 1
    return bot


def calc_col(s):
    top = 7
    bot = 0
    for c in s:
        if c == 'L':
            top = bot + int(((top - bot) / 2))
        elif c == 'R':
            bot = bot + int(((top - bot) / 2)) + 1
    return top


highest = 0
seats = []
for line in data:
    row = calc_row(line)
    col = calc_col(line)
    seat_id = (row * 8) + col
    highest = max(highest, seat_id)
    seats.append(seat_id)

print(f"part1: {highest}")

for seat in range(0, highest):
    if seat not in seats:
        if seat - 1 in seats and seat + 1 in seats:
            print(f"part2: {seat}")
