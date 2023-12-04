from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    def setup(self):
        self.modules = list(map(int, self.lines))

    def part_one(self):
        return sum(x // 3 - 2 for x in self.modules)

    def part_two(self):
        return sum(self.calculate(x) for x in self.modules)

    def calculate(self, mass):
        fuel = mass // 3 - 2

        if fuel < 0:
            return 0

        return fuel + self.calculate(fuel)
