from aoc.lib.base_solution import BaseSolution

import itertools


class Solution(BaseSolution):
    result_one = 51833
    result_two = 288

    def setup(self):
        self.numbers = []

        for line in self.lines:
            numbers = list(map(int, line.split()))
            self.numbers.append(numbers)

    def part_one(self):
        total = 0

        for numbers in self.numbers:
            total += max(numbers) - min(numbers)

        return total

    def part_two(self):
        total = 0

        for numbers in self.numbers:
            pairs = itertools.product(numbers, numbers)

            for n1, n2 in pairs:
                if n1 == n2: continue

                div, mod = divmod(n1, n2)
                if mod == 0:
                    total += div
                    break

        return total
