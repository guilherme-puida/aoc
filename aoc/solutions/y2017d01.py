from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    result_one = 1119
    result_two = 1420
    
    def setup(self):
        self.input_len = len(self.input_str)
        pass

    def part_one(self):
        total = 0

        for i, c in enumerate(self.input_str):
            if c == self.input_str[(i + 1) % self.input_len]:
                total += int(c)

        return total

    def part_two(self):
        total = 0

        for i, c in enumerate(self.input_str):
            if c == self.input_str[(i + (self.input_len // 2)) % self.input_len]:
                total += int(c)

        return total
