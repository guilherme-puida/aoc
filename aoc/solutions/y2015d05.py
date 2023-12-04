from aoc.lib.base_solution import BaseSolution

import re


class Solution(BaseSolution):
    def setup(self):
        pass

    def part_one(self):
        total = 0

        for line in self.lines:
            vowels = len(re.findall(r"[aeiou]", line))
            twice = len(re.findall(r"(.)\1", line))
            not_allowed = len(re.findall(r"ab|cd|pq|xy", line))

            if vowels >= 3 and twice > 0 and not_allowed == 0:
                total += 1

        return total

    def part_two(self):
        total = 0

        for line in self.lines:
            pair = len(re.findall(r"(.)(.).*\1\2", line))
            repeat = len(re.findall(r"(.).\1", line))

            if pair and repeat:
                total += 1

        return total
