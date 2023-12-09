from pathlib import Path
from typing import Literal, Dict, List

data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]
data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


def parse_game(lines: List[str]) -> Dict[str, List[Dict[Literal['green', 'blue', 'red'], int]]]:
    ret = {}
    for line in lines:
        game, line = line.split(':')
        ret[game] = []
        for rnd in line.strip().split(';'):
            rnd_result = {}
            for entry in rnd.split(','):
                count, color = entry.strip().split(' ')
                rnd_result[color] = count
            ret[game].append(rnd_result)

    return ret


def part1():
    sum = 0
    games = parse_game(data)
    for name, game in games.items():
        valid = True
        for rnd in game:
            red = int(rnd.get('red', 0))
            green = int(rnd.get('green', 0))
            blue = int(rnd.get('blue', 0))
            if red > 12:
                valid = False
            if green > 13:
                valid = False
            if blue > 14:
                valid = False
            if not valid:
                break
        if valid:
            n = int(name.split(' ')[1])
            # print('game valid!', name, n)
            sum += n

    return sum


def part2():
    sum = 0
    games = parse_game(data)
    for name, game in games.items():
        red = 0
        green = 0
        blue = 0
        for rnd in game:
            red = max(red, int(rnd.get('red', 0)))
            green = max(green, int(rnd.get('green', 0)))
            blue = max(blue, int(rnd.get('blue', 0)))
        # print(name, red, green, blue, red * green * blue)
        sum += red * green * blue
    return sum



print(f"part1: {part1()}")
print(f"part2: {part2()}")
