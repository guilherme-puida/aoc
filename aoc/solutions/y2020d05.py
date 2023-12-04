from aoc.lib.base_solution import BaseSolution

import itertools


class Solution(BaseSolution):
    result_one = 818
    result_two = 559

    def setup(self):
        pass

    def part_one(self):
        return max(self.calculate_ids())

    def part_two(self):
        ids = sorted(self.calculate_ids())

        for i1, i2 in itertools.pairwise(ids):
            if i1 + 2 == i2:
                return i1 + 1


    def calculate_ids(self):
        ids = []

        for line in self.lines:
            rows = list(range(128))
            cols = list(range(8))

            for char in line:
                lrows = len(rows) // 2
                lcols = len(cols) // 2

                if char == "F":
                    rows = rows[:lrows]
                if char == "B":
                    rows = rows[lrows:]
                if char == "L":
                    cols = cols[:lcols]
                if char == "R":
                    cols = cols[lcols:]

            assert len(rows) == 1 and len(cols) == 1

            ids.append(rows[0] * 8 + cols[0])

        return ids
