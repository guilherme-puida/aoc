from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    def setup(self):
        pass

    def part_one(self):
        total = 0

        for line in self.lines:
            total += len(line) - len(eval(line))

        return total

    def part_two(self):
        total = 0

        for line in self.lines:
            total += line.count("\\") + line.count('"') + 2

        return total
