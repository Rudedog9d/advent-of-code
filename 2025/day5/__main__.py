from pathlib import Path
from typing import Sequence, Iterable

data = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]
# data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]

LineData = list[list[int]]
Rules = dict[int, list]

def parse_data() -> tuple[Rules, LineData]:
    rules: dict[int, list] = {}
    lines = []
    for line in data:
        if not line:
            continue
        if '|' in line:
            x, y = map(int, line.split('|'))
            if x in rules:
                rules[x].append(y)
            else:
                rules[x] = [y]
        else:
            lines.append(list(map(int, line.split(','))))
    return rules, lines

def validate_line(rules: Rules, line: list[int]) -> bool:
    # reverse line so we don't need to walk backwards
    line = list(reversed(line))
    for i, n in enumerate(line):
        if n not in rules:
            continue
        for m in line[i + 1:]:
            if m in rules[n]:
                print(f'invalid: {n=} {m=} line={" ".join(map(str, line))}\trule={" ".join(map(str, rules[n]))}')
                return False
    return True

def validate_lines(rules: Rules, lines: LineData) -> tuple[LineData, LineData]:
    correct = []
    incorrect = []
    for line in lines:
        valid = validate_line(rules, line)
        if valid:
            correct.append(line)
        else:
            incorrect.append(line)
    return correct, incorrect


def fix_line(line: list[int], rules: Rules) -> list[int]:
    # while not validate_line(rules, line):
        rev_line = list(reversed(line))
        # for i in range(len(line) - 1, 0, -1):
        for i, n in enumerate(rev_line):
            # n = line[i]
            if n not in rules:
                continue
            for j, m in enumerate(rev_line[i+1:]):
                if m in rules[n]:
                    # this is true:  l[i - len(l)] == l[i]
                    idx = i - len(line)
                    jdx = j - len(line)
                    print(f'{i=} {j=} {idx=} {jdx=}')
                    print(f'needs fixed: {n=} {m=} n=line[{idx}]={line[idx]} m=line[{jdx}]={line[jdx]} line={" ".join(map(str, line))}\trule[{n}]={" ".join(map(str, rules[n]))}')
                    # what if we just swap 'em?
                    line[jdx] = n
                    line[idx] = m
                    # m is breaking here
                    # n is the rule
                    # so n needs to be after m?
    # return line

def part1():
    rules, lines = parse_data()
    lines, _ = validate_lines(rules, lines)
    # total = 0
    # for line in lines:
    #     # get middle of list
    #     start = int((len(line) / 2))
    #     total += line[start]
    return sum(line[int((len(line) / 2))] for line in lines)

def part2():
    rules, lines = parse_data()
    _, lines = validate_lines(rules, lines)
    lines = [fix_line(line, rules) for line in lines]
    return sum(line[int((len(line) / 2))] for line in lines)


print(f"part1: {part1()}")
print(f"part2: {part2()}")
