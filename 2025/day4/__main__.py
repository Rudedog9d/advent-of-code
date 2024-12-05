from pathlib import Path

from pydantic import BaseModel

data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX",
]
data = [line.strip() for line in open(Path(Path(__file__).parent, 'input.txt'))]


class Word(BaseModel):
    word: str
    # starting position for the word
    start: tuple[int, int]
    end: tuple[int, int]


def extend_offset(n: int) -> int:
    """Extend the offset by 1, determining direction by int sign"""
    if n < 0:
        return n + 1
    if n > 0:
        return n + 1
    return n


def print_dir(directions: list[tuple[int, int] | bool]):
    print(directions[0:3], directions[3:6], directions[6:9], sep='\n')

x_dir = {-1: 'left', 0: '', 1: 'right'}
y_dir = {
    -1: 'up',
    0: '',
    1: 'down',
}


class WordSearch(BaseModel):
    data: list[str]

    def get(self, y: int, x: int) -> str | None:
        if x < 0 or y < 0:
            # large numbers will throw an index error, but small numbers will return from the end of a list
            return None

        try:
            return self.data[y][x]
        except IndexError:
            return None

    def find_str_from_start(self, x: int, y: int, text: str) -> int:
        directions: list[tuple[int, int]] = [
            # tuples are x, y
            (-1, -1), (0, -1), (1, -1),
            (-1, 0),           (1, 0),
            (-1, 1),  (0, 1),  (1, 1),
        ]
        words = 0
        for x_off, y_off in directions:
            word = ''
            for i in range(len(text)):
                letter = self.get(y=y + (y_off * i), x=x + (x_off * i))
                if not letter:
                    break
                word += letter

            if word == text:
                words += 1

        return words

    def _find_x_mas(self, x: int, y: int) -> bool:
        end = 'MS'
        directions = [
            # tuples are x,y
            [(-1, -1), (1, 1)],
            [[1, -1], (-1, 1)]
        ]
        valid = True
        for row in directions:
            dir_a, dir_b = row
            letter_a = self.get(x=x + (dir_a[0]), y=y + (dir_a[1]))
            letter_b = self.get(x=x + (dir_b[0]), y=y + (dir_b[1]))
            valid &= bool(letter_a and letter_b and letter_a in end and letter_b in end and letter_a != letter_b)
        return valid

    def find_x_mas(self):
        y = 0
        count = 0
        while y < len(self.data):
            x = 0
            while x < len(self.data[y]):
                if self.get(x=x, y=y) == 'A' and self._find_x_mas(x, y):
                    count += 1
                x += 1
            y += 1
        return count

    def find_word(self, word: str):
        y = 0
        count = 0
        while y < len(self.data):
            x = 0
            while x < len(self.data[y]):
                if self.get(x=x, y=y) == word[0]:
                    count += self.find_str_from_start(x, y, word)
                x += 1
            y += 1
        return count

def part1():
    search = WordSearch(data=data)
    return search.find_word("XMAS")


def part2():
    search = WordSearch(data=data)
    return search.find_x_mas()


print(f"part1: {part1()}")
print(f"part2: {part2()}")




















