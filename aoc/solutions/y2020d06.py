from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    result_one = 6596
    result_two = 3219

    def setup(self):
        self.groups = self.input_str.split("\n\n")

    def part_one(self):
        total = 0
        
        for group in self.groups:
            group = group.replace("\n", "")
            total += len(set(group))

        return total

    def part_two(self):
        total = 0

        for group in self.groups:
            answers = [set(x) for x in group.splitlines()]
            total += len(set.intersection(*answers))

        return total
