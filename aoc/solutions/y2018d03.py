from aoc.lib.base_solution import BaseSolution

import collections
import itertools
import re


line_regex = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")


class Solution(BaseSolution):
    def setup(self):
        self.squares = {}
        for line in self.lines:
            id, x, y, width, length = map(int, line_regex.match(line).groups())
            self.squares[id] = self.get_square(x, y, width, length)

        self.grid = collections.defaultdict(int)

        for id, square in self.squares.items():
            for pos in square:
                self.grid[pos] += 1

    def part_one(self):
        return sum(1 for x in self.grid.values() if x >= 2)

    def part_two(self):
        for id, square in self.squares.items():
            if all(self.grid[pos] == 1 for pos in square):
                return id

    def get_square(self, x, y, width, length):
        xs = range(x, x + width)
        ys = range(y, y + length)

        return list(itertools.product(xs, ys))
