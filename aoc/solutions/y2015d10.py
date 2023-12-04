from aoc.lib.base_solution import BaseSolution

import itertools


class Solution(BaseSolution):
    def setup(self):
        pass

    def part_one(self):
        current = self.input_str

        for _ in range(40):
            current = self.step(current)

        self.result = current
        return len(current)

    def part_two(self):
        if not self.result:
            self.part_one()

        current = self.result

        for _ in range(10):
            current = self.step(current)

        return len(current)

    def step(self, current):
        g = [(k, sum(1 for _ in g)) for k, g in itertools.groupby(current)]
        return "".join(f"{count}{char}" for char, count in g)
