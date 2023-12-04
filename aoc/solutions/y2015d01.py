from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    result_one = 280
    result_two = 1797

    def setup(self):
        self.floors = [0]

        for char in self.input_str:
            offset = 1 if char == "(" else -1
            self.floors.append(self.floors[-1] + offset)

    def part_one(self):
        return self.floors[-1]

    def part_two(self):
        for i, floor in enumerate(self.floors):
            if floor < 0:
                return i
