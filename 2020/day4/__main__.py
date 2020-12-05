from pathlib import Path
from typing import Dict
import re

data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


def is_valid_part_1(pp: Dict):
    keys = pp.keys()
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:  # 'cid' is temporarily omitted :D
        if key not in keys:
            return False
    return True


def validate_num(min, v, max):
    return


def is_valid_part_2(pp: Dict):
    validators = {
        'byr': lambda v: 1920 <= int(v) <= 2002,
        'iyr': lambda v: 2010 <= int(v) <= 2020,
        'eyr': lambda v: 2020 <= int(v) <= 2030,
        'hgt': lambda v:
        (
                v.endswith('cm') and (150 <= int(v[:-2]) <= 193)
        ) or (
                v.endswith('in') and (59 <= int(v[:-2]) <= 76)
        ),
        'hcl': lambda v: re.match('^#[0-9a-f]{6}$', v),
        'ecl': lambda v: v in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda v: re.match('^[0-9]{9}$', v),
    }
    keys = pp.keys()
    for key, validator in validators.items():  # 'cid' is temporarily omitted :D
        if key not in keys:
            print(f'missing {key}:\t {keys}')
            return False
        if not validator(pp[key]):
            print(f'failed {key}:\t {keys}')
            return False
    print(f'valid: \t\t{keys}')
    return True


def parse(line):
    d = {}
    for entry in line.split():
        entry = entry.split(':')
        d[entry[0]] = entry[1]
    return d


def iter_data(validator):
    num_valid = 0
    passport = {}
    for line in data:
        if not line:
            num_valid += 1 if validator(passport) else 0
            passport = {}
            continue
        passport.update(parse(line))
    num_valid += 1 if validator(passport) else 0  # handle final entry
    return num_valid


print(f"part1: {iter_data(is_valid_part_1)}")
print(f"part2: {iter_data(is_valid_part_2)}")
