from math import ceil, floor
# data = 76
data = 368078

'''
Part 1
'''
def find_row_size(n):
    ret = 1
    num_rows = 1
    while ret * ret < n:
        ret += 2
        num_rows += 1
    return ret, num_rows

matrix_size, num_rows = find_row_size(data)
max_size = matrix_size * matrix_size

horiz_middle = ceil(matrix_size / 2)
horiz_pos = matrix_size - (max_size - data)
horiz_jumps = abs(horiz_pos - horiz_middle)

vert_jumps = floor(matrix_size / 2)

print('{}x{}, num rows={}, row max = {}'.format(matrix_size, matrix_size, num_rows, matrix_size * matrix_size))
print('Part 1:', horiz_jumps + vert_jumps)


'''
Part 2
'''
class blah():
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.matrix_size = 0
        # Start with some data already defined, to lazy to code start case
        self.x = self.y = 2
        self.matrix = [
            [5,   4,   2],
            [10,  1,   1],
            [11,  23,  25]
        ]

    def add_rows(self):
        # Increase indexes to match
        self.x += 1
        self.y += 1
        # Add empty row to top
        self.matrix.insert(0, [0 for _ in range(0, self.matrix_size + 1)])
        # Add empty row to bottom
        self.matrix.append([0 for _ in range(0, self.matrix_size + 1)])
        for row in self.matrix:
            # Add column to beginning of all rows
            row.insert(0, 0)
            # Add column to end of all rows
            row.append(0)

    def print_matrix(self):
        print('=' * 102)
        for row in self.matrix:
            for v in row:
                print('{}'.format(v).ljust(8), end='\t')
            print()
        print('=' * 102)

    def generate_new_val(self):
        # create locals for easy reading
        x = self.x
        y = self.y
        ret = 0

        # Verticals
        if y > 0:
            ret += self.matrix[y - 1][x]
        if y < self.matrix_size:
            ret += self.matrix[y + 1][x]

        # Horizontals
        if x > 0:
            ret += self.matrix[y][x - 1]
        if x < self.matrix_size:
            ret += self.matrix[y][x + 1]

        # Diagonals
        if x > 0:
            if y > 0:
                ret += self.matrix[y - 1][x - 1]  # top left diag
            if y < self.matrix_size:
                ret += self.matrix[y + 1][x - 1]  # bottom left diag

        if x < self.matrix_size:
            if y > 0:
                ret += self.matrix[y - 1][x + 1]
            if y < self.matrix_size:
                ret += self.matrix[y + 1][x + 1]

        return ret

    def move_up(self,):
        self.y -= 1

    def move_down(self,):
        self.y += 1

    def move_right(self,):
        self.x += 1

    def move_left(self,):
        self.x -= 1

    def run(self, target):
        while self.matrix[self.y][self.x] < target:
            self.matrix_size = len(self.matrix) - 1
            if self.verbose:
                print('{}x{}={}'.format(self.y, self.x, self.matrix[self.y][self.x]))
                self.print_matrix()
            if self.x == 0:
                '''
                Left Column
                '''
                if self.y == self.matrix_size:
                    # move right, bottom left corner
                    self.move_right()
                else:
                    # move down
                    self.move_down()
            elif self.y == self.matrix_size:
                '''
                Bottom Row
                '''
                if self.x == self.matrix_size:
                    self.add_rows()
                    self.move_right()
                else:
                    # Bottom row
                    self.move_right()
            elif self.x == self.matrix_size:
                '''
                Right Column
                '''
                if self.y == 0:
                    # Top right corner
                    self.move_left()
                else:
                    # Right column, travelling up
                    self.move_up()
            elif self.y == 0:
                '''
                Top Row
                '''
                if self.x == 0:
                    # top left corner, move down
                    self.move_down()
                else:
                    # bottom row, move right
                    self.move_left()
            else:
                raise Exception("Not sure what to do with {}x{}".format(self.x, self.y))

            # Set new value
            self.matrix[self.y][self.x] = self.generate_new_val()

        # Return winning value!
        return self.matrix[self.y][self.x]

ret = blah().run(data)
# ret = blah(verbose=True).run(data)
print('Part 2:', ret)
