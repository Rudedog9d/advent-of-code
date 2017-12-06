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
    def __init__(self):
        self.data = 806
        self.matrix = [
            [5,   4,   2],
            [10,  1,   1],
            [11,  23,  25]
        ]
        self.matrix_size = 0
        self.n = 1
        self.x = self.y = 0

    def add_up(self):
        pass

    def add_down(self):
        pass

    def add_left(self):
        pass

    def add_right(self):
        pass

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
        print('=' * 10)
        for row in self.matrix:
            for v in row:
                print('{}\t'.format(v), end='')
            print()
        print('=' * 10)

    def generate_new_val(self):
        pass

    def move_up(self,):
        self.y -= 1
        # val = self.matrix[self.y][self.x]
        # self.matrix[self.y][self.x]
        # print('{}x{}={}'.format(self.y, self.x, self.matrix[self.y][self.x]))

    def move_down(self,):
        self.y += 1
        # print('{}x{}={}'.format(self.y, self.x, self.matrix[self.y][self.x]))

    def move_right(self,):
        self.x += 1
        # val = self.generate_new_val()
        # self.matrix[self.y].append(val)
        # print('{}x{}={}'.format(self.y, self.x, self.matrix[self.y][self.x]))

    def move_left(self,):
        self.x -= 1
        # val = self.generate_new_val()
        # self.matrix[self.y][self.x] = val
        # print('{}x{}={}'.format(self.y, self.x, self.matrix[self.y][self.x]))

    def run(self):
        while self.n < data:
            self.matrix_size = len(self.matrix) - 1
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


blah().run()


































