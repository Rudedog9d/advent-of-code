from pathlib import Path

sample_data = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]

# todo read in data

data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


def calculate_trees(data, x_offset, y_offset):
    max_x = len(data[0])
    x = 0
    y = 0
    trees = 0
    while True:
        x += x_offset
        y += y_offset
        if x >= max_x:
            x -= max_x

        if y > len(data) - 1:
            return trees

        if data[y][x] == '#':
            trees += 1


total_trees = 1
pairs = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

print(f"part1: {calculate_trees(data, 3, 1)}")
for x, y in pairs:
    total_trees *= calculate_trees(data, x, y)

print(f"part2: {total_trees}")
