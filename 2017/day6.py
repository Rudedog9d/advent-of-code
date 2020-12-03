'''
Real Data
'''
# Read in first line of data only
line = open('day6-input.txt').readlines()[0].strip()
data = [int(x) for x in line.split()]

'''
Example Data
'''
# data = [0, 2, 7, 0]

'''
Constants
'''
PRINT_VERBOSE = False
BANK_COUNT = len(data)  # Get Bank Count

def print_debug(data, index):
    if not PRINT_VERBOSE: return
    print('{}: {}'.format(index, data))

'''
Part 1
'''
# Start history file with data
history = [data.copy()]
found = False
cnt = 0

while not found:
    # Increment Count
    cnt += 1

    # Find bank to redistribute
    i = data.index(max(data))

    # Print for Debugging :)
    print_debug(data, i)

    # Get Blocks and zero the Bank
    blocks = data[i]
    data[i] = 0

    # Do Redistribution
    while blocks:
        # Wrap around to beginning if at end of list
        i = i + 1 if i + 1 < BANK_COUNT else 0
        data[i] += 1
        blocks -= 1

    # Check in history for duplicate
    if data in history:
        # If found, break and print [D]one
        found = True
        print_debug(data, 'D')
    else:
        # Else, append copy (not reference...) of current list to history
        history.append(data.copy())

print('Part 1:', cnt)

'''
Part 2
'''
# Find distance between first sighting and second
print('Part 2:', len(history) - history.index(data))
