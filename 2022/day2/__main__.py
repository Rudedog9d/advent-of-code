from pathlib import Path

data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]
# data = """
# A X
# A Y
# A Z
# B X
# B Y
# B Z
# C X
# C Y
# C Z
# """.split('\n')
# data = """
# A Y
# B X
# C Z
# """.split('\n')

#
val_map = {
    'A': 1,
    'X': 1,
    'B': 2,
    'Y': 2,
    'C': 3,
    'Z': 3,
}

def print_result(player, opponent, score):
    strings = {
        1: 'rock',
        2: 'paper',
        3: 'scissors'
    }
    print(f"{strings[player]}\t{strings[opponent]}\t{score}")


def calc_score(player: int, opponent: int):
    score = player

    # first check for a draw
    if player == opponent:
        score += 3
    # otherwise, check for the player's winning cases
    elif player == 1 and opponent == 3:
        score += 6
    elif player == 2 and opponent == 1:
        score += 6
    elif player == 3 and opponent == 2:
        score += 6
    # print_result(player, opponent, score)
    return score


def part1():
    total = 0
    for line in data:
        if not line: continue
        # parse line
        opponent, player  = line.split(' ')
        player = val_map[player]
        opponent = val_map[opponent]
        # calculate score
        total += calc_score(player, opponent)
    return total


def part2():
    total = 0
    for line in data:
        if not line: continue
        # Parse Line
        opponent, action = line.split(' ')
        opponent = val_map[opponent]

        # determine player hand based on action
        if action == 'X':  # must lose
            player = opponent - 1
        elif action == 'Y': # must tie
            player = opponent
        else: # must win
            player = opponent + 1

        # handle upper/lower bounds
        if player == 0: player = 3
        if player == 4: player = 1

        # calculate score
        total += calc_score(player, opponent)
    return total


print(f"part1: {part1()}")
print(f"part2: {part2()}")
