from aoc.lib.base_solution import BaseSolution

import itertools


class Solution(BaseSolution):
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
