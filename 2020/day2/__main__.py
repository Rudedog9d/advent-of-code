from pathlib import Path

data = [
    "1-3 a: abcde",
    "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]


def get_letter(string, pos):
    if len(string) > pos:
        return string[pos]
    return '😭'


down_the_street_valid = 0
toboggan_corporate_valid = 0
# for line in data:
for line in open(Path(Path(__file__).parent, 'input.txt')):
    values = line.split(' ')

    min_val, max_val = values[0].split('-')
    min_val, max_val = int(min_val), int(max_val)
    letter = values[1].split(':')[0]
    passwd = values[2].strip()

    if min_val <= passwd.count(letter) <= max_val:
        down_the_street_valid += 1

    min_val -= 1
    max_val -= 1

    if (get_letter(passwd, min_val) == letter) ^ (get_letter(passwd, max_val) == letter):
        toboggan_corporate_valid += 1

print("part 1: {} valid passwords".format(down_the_street_valid))
print("part 2: {} valid passwords".format(toboggan_corporate_valid))

