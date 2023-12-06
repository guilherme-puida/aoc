from aoc.lib.base_solution import BaseSolution

import math


class Solution(BaseSolution):
    result_one = 512295
    result_two = 36530883

    def setup(self):
        self.races = []

        for t, d in zip(*(line.split()[1:] for line in self.lines)):
            self.races.append((int(t), int(d)))

    def part_one(self):
        return math.prod(self.calculate(time, distance) for time, distance in self.races)

    def part_two(self):
        time = int(''.join(str(t) for t, _ in self.races))
        distance = int(''.join(str(d) for _, d in self.races))

        return self.calculate(time, distance)

    def calculate(self, time, distance):
        delta = math.sqrt(time ** 2 - (4 * distance))
        x1 = (-time - delta) // -2
        x2 = (-time + delta) // -2

        return int(x1 - x2)
