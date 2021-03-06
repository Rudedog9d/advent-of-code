from pathlib import Path
import re

data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]

# Sample Data 1
# data = [
#     "light red bags contain 1 bright white bag, 2 muted yellow bags.",
#     "light red bags contain 1 bright white bag, 2 muted yellow bags.",
#     "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
#     "bright white bags contain 1 shiny gold bag.",
#     "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
#     "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
#     "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
#     "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
#     "faded blue bags contain no other bags.",
#     "dotted black bags contain no other bags."
# ]

# Sample Data 2
# data = [
#     "shiny gold bags contain 2 dark red bags.",
#     "dark red bags contain 2 dark orange bags.",
#     "dark orange bags contain 2 dark yellow bags.",
#     "dark yellow bags contain 2 dark green bags.",
#     "dark green bags contain 2 dark blue bags.",
#     "dark blue bags contain 2 dark violet bags.",
#     "dark violet bags contain no other bags."
# ]

rules = {
    # 'light_red': {
    #     'bright_white': 1,
    #     'muted_yellow': 2
    # }
}


def add_rule(name, match: re.Match):
    if not rules.get(name):
        rules[name] = {}
    rules[name][match.group(2)] = int(match.group(1))


def build_rules():
    bag_re = re.compile(r"([0-9]) ([a-z]+ [a-z]+) bags?")
    for line in data:
        parts = line.split()
        rule_name = f"{parts[0]} {parts[1]}"
        # find first rule, if it exists (will not match 'contains no other bags')
        rule = bag_re.search(line)
        while rule:
            # Add the rule, if we found a match (from before the loop or inside)
            add_rule(rule_name, rule)
            # Find the next rule, using the end of our current match as the starting position
            rule = bag_re.search(line, pos=rule.end())


def find_bag(rule, bag):
    """
    Search `rule` and check if it contains `bag`
    :param rule: Rule to search (a bag name)
    :param bag: Bag to search for (a bag name)
    :return bool: True if `bag` was found within `rule`
    """
    for sub_rule in rules.get(rule, []):
        if sub_rule == bag:
            return True
        if find_bag(sub_rule, bag):
            return True
    return False


def count_bags(rule):
    """
    Count number of nested bags within `rule`
    """
    count = 0
    for sub_rule in rules.get(rule, []):
        # Get number of sub-bags in this rule
        num = rules[rule].get(sub_rule)
        # return number of sub_rule bags + (all bags with EACH sub_rule)
        count += num + (num * count_bags(sub_rule))
    return count


build_rules()
print(f"part1: {sum([find_bag(r, 'shiny gold') for r in rules])}")
print(f"part2: {count_bags('shiny gold')}")
