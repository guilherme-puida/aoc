from aoc.lib.base_solution import BaseSolution

import itertools


class Solution(BaseSolution):
    result_one = 10228230
    result_two = 447073334102

    def setup(self):
        self.rows = [list(x) for x in self.lines]
        self.cols = list(map(list, zip(*self.rows)))

        self.empty_rows = [i for i, e in enumerate(self.rows) if '#' not in e]
        self.empty_cols = [i for i, e in enumerate(self.cols) if '#' not in e]

        self.galaxies = [(x, y) for x, row in enumerate(self.rows) for y, char in enumerate(row) if char == '#']

    def part_one(self):
        return self.solve(1)
        
    def part_two(self):
        return self.solve(1_000_000 - 1)

    def solve(self, expansion_factor):
        total = 0

        for (row1, col1), (row2, col2) in itertools.combinations(self.galaxies, 2):
            small_row, big_row = min(row1, row2), max(row1, row2)
            small_col, big_col = min(col1, col2), max(col1, col2)

            added_rows = sum(expansion_factor for row in self.empty_rows if small_row <= row < big_row)
            added_cols = sum(expansion_factor for col in self.empty_cols if small_col <= col < big_col)

            total += big_row - small_row + big_col - small_col + added_rows + added_cols

        return total
