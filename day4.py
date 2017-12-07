import collections

data = [line for line in open('day4-input.txt')]
print('Length of data:', len(data))

'''
Part 1
'''
def is_valid(line):
    words = []
    for word in line.split():
        if word in words:
            return False
        words.append(word)
    return True

valid = 0
for line in data:
    if is_valid(line):
        valid += 1

print('Part 1:', valid)

'''
Part 2
'''
def is_valid(line):
    words = []
    for x in line.split():
        for y in words:
            if len(x) == len(y) and collections.Counter([c for c in x]) == collections.Counter([c for c in y]):
                return False
        words.append(x)
    return True

valid = 0
for line in data:
    if is_valid(line):
        valid += 1

print('Part 2:', valid)
