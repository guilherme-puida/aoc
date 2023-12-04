from aoc.lib.base_solution import BaseSolution

import itertools


class Solution(BaseSolution):
    result_one = 569
    result_two = 77666

    def setup(self):
        pass

    def part_one(self):
        total = 0

        for line in self.lines:
            total += int(line)

        return total

    def part_two(self):
        total = 0
        seen = {total}
        
        for line in itertools.cycle(self.lines):
            total += int(line)
            if total in seen:
                return total
            seen.add(total)
