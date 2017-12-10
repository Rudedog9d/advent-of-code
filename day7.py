import collections

'''
Real Data
'''
# Read in first line of data only
data = open('day7-input.txt').readlines()

'''
Example Data
                          gyxo (61)
                        /
              ugml (68) - ebii (61)
            /           \ 
           |              jptl (61)
           |        
           |              pbga (66)
          /             / 
tknk (41) --- padx (45) - havc (66)
          \             \ 
           |              qoyq (66)
           |             
           |              ktlj (57)
            \           /
              fwft (72) - cntj (57)
                        \ 
                          xhth (57)
'''
# data = [
#     'pbga (66)',
#     'xhth (57)',
#     'ebii (61)',
#     'havc (66)',
#     'ktlj (57)',
#     'fwft (72) -> ktlj, cntj, xhth',
#     'qoyq (66)',
#     'padx (45) -> pbga, havc, qoyq',
#     'tknk (41) -> ugml, padx, fwft',
#     'jptl (61)',
#     'ugml (68) -> gyxo, ebii, jptl',
#     'gyxo (61)',
#     'cntj (57)'
# ]

'''
Constants
'''
PRINT_VERBOSE = False

class Program:
    def __init__(self, name, weight, children=None):
        self.name = name
        self.weight = weight
        self.children = children or []

    @classmethod
    def parse(cls, string):
        '''
        Parse a string into a Program Object
        :param str string: String to parse
        :return Program:
        '''
        parts = string.split()
        name = None
        weight = None
        children = []
        for i,part in enumerate(parts):
            if i == 0:
                name = part
            elif i == 1:
                # Convert to int (remove parens first)
                weight = int(part[1:-1])
            # Skip index 2 because it is an Arrow ->
            elif i > 2:
                children.append(part.replace(',', ''))
        return Program(name, weight, children)

    @property
    def disk_weight(self):
        d_weight = 0
        for child in self.children:
            d_weight += child.weight + child.disk_weight
        return d_weight

    @property
    def is_balanced(self):
        if not self.children: return True

        t = self.children[0].disk_weight + self.children[0].weight
        for child in self.children:
            if child.weight + child.disk_weight != t:
                return False
        return True

    def __eq__(self, other):
        '''
        Check if two program objects are equal
        :param Program other:
        :return bool:
        '''
        return (type(other) == type(self)
                and self.name == other.name
                and self.weight == other.weight
                and self.children == self.children)



def print_debug(data, index):
    if not PRINT_VERBOSE: return
    print('{}: {}'.format(index, data))

'''
Part 1
'''
programs = []
for x in data:
    programs.append(Program.parse(x))

root = None
for prog in programs:
    parent = None
    for prog2 in programs:
        if prog == prog2: continue
        if prog.name in prog2.children:
            parent = prog2
            break
    if not parent:
        root = prog
        break

print('Part 1:', root.name)

'''
Part 2 - Find mis-weighted program
'''
def check_balance(prog):
    weights = {}
    min = 0
    for i,child in enumerate(prog.children):
        weights[child] = child.disk_weight()
        min = weights[child] if weights[child] > min else '?'
    # counts = collections.Counter([x for x in weights.values()])
    # print(min(counts)


check_balance(root)
print('Part 2:', '?')































