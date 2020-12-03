'''
Real Data
'''
data = open('day8-input.txt').readlines()

'''
Example Data
'''
# data = [
#     'b inc 5 if a > 1',
#     'a inc 1 if b < 5',
#     'c dec -10 if a >= 1',
#     'c inc -20 if c == 10'
# ]

'''
Constants
'''
PRINT_VERBOSE = False
FUNCS = {
    '>': lambda a,b: a > b,
    '>=': lambda a,b: a >= b,
    '<': lambda a,b: a < b,
    '<=': lambda a,b: a <= b,
    '==': lambda a,b: a == b,
    '!=': lambda a,b: a != b,
    'inc': lambda a,b: a + b,
    'dec': lambda a,b: a - b
}

def print_debug(data):
    if not PRINT_VERBOSE: return
    print('{}'.format(data))

'''
Part 1 - Parse Registers and implement action
'''
registers = {}
part2 = 0

for line in data:
    print_debug('line: {}'.format(line))
    reg, op, val, _, con_reg, con_op, con_val = line.split()
    if FUNCS[con_op](registers.get(con_reg, 0), int(con_val)):
        registers[reg] = FUNCS[op](registers.get(reg, 0), int(val))
    part2 = max(part2, registers.get(reg, 0))

print('Part 1:', max(registers.values()))

'''
Part 2 - Track what the largest value was throughout the operations
'''
print('Part 2:', part2)
