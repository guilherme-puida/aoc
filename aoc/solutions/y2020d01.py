from aoc.lib.base_solution import BaseSolution

import itertools


class Solution(BaseSolution):
    result_one = 980499
    result_two = 200637466

    def setup(self):
        self.numbers = list(map(int, self.lines))

    def part_one(self):
        for n1, n2 in itertools.product(self.numbers, self.numbers):
            if n1 == n2:
                continue

            if n1 + n2 == 2020:
                return n1 * n2

    def part_two(self):
        for n1, n2, n3 in itertools.product(self.numbers, self.numbers, self.numbers):
            if n1 == n2 or n1 == n3 or n2 == n3:
                continue

            if n1 + n2 + n3 == 2020:
                return n1 * n2 * n3
