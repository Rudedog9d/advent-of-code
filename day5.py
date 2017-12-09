# Two copies because the data gets modified and lists are referenced in python
data = [int(x.strip()) for x in open('day5-input.txt')]
data2 = [int(x.strip()) for x in open('day5-input.txt')]

# data = [0, 3, 0, 1, -3]
# data2 = [0, 3, 0, 1, -3]

PRINT_VERBOSE = False

def print_debug(data, index):
    if not PRINT_VERBOSE: return
    for i,x in enumerate(data):
        if index == i:
            print('({})'.format(x), end=' ')
        else:
            print(x, end=' ')
    print()

'''
Part 1
'''
found = False
cnt = 0
i = jmp = 0
while not found:
    print_debug(data, i)

    # Increment counter for answer
    cnt += 1

    # Get Current Jump
    jmp = data[i]

    # Increment jump at current location
    data[i] = jmp + 1

    # Set new location
    i = i + jmp
    try:
        # Try to access Array - if out of bounds, answer found
        _ = data[i]
    except IndexError as e:
        print_debug(data, i)
        found = True

print('Part 1:', cnt)


'''
Part 2
'''
found = False
cnt = 0
i = jmp = 0
while not found:
    print_debug(data2, i)

    # Increment counter for answer
    cnt += 1

    # Get Current Jump
    jmp = data2[i]

    # Increment jump at current location
    data2[i] = jmp + (1 if jmp < 3 else -1)
    # print(jmp, data[i])

    # Set new location
    i = i + jmp
    try:
        # Try to access Array - if out of bounds, answer found
        _ = data2[i]
    except IndexError as e:
        print_debug(data2, i)
        found = True

print('Part 2:', cnt)
