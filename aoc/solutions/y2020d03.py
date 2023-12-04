from aoc.lib.base_solution import BaseSolution

import itertools


class Solution(BaseSolution):
    result_one = 259
    result_two = 2224913600

    def setup(self):
        self.width = len(self.lines[0])
        self.height = len(self.lines)

    def part_one(self):
        return self.solve([(1, 3)])

    def part_two(self):
        slopes = [
            (1, 1),
            (1, 3),
            (1, 5),
            (1, 7),
            (2, 1),
        ]

        return self.solve(slopes)

    def solve(self, slopes):
        total = 1

        for row_step, col_step in slopes:
            trees = 0
            positions = zip(
                range(0, self.height, row_step),
                itertools.count(start=0, step=col_step)
            )

            for row, col in positions:
                if self.lines[row][col % self.width] == "#":
                    trees += 1

            total *= trees

        return total
