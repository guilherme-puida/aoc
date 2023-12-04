from aoc.lib.base_solution import BaseSolution

import collections
import re


line_regex = re.compile(r"(\d+)-(\d+) (\w): (\w+)")

class Solution(BaseSolution):
    result_one = 628
    result_two = 705

    def setup(self):
        self.entries = []

        for line in self.lines:
            min_amount, max_amount, char, password = line_regex.match(line).groups()
            self.entries.append((int(min_amount), int(max_amount), char, password))

    def part_one(self):
        total = 0

        for min_amount, max_amount, char, password in self.entries:
            counter = collections.Counter(password)
            if min_amount <= counter[char] <= max_amount:
                total += 1

        return total

    def part_two(self):
        total = 0

        for p1, p2, char, password in self.entries:
            if sum(1 for x in [p1, p2] if password[x - 1] == char) == 1:
                total += 1

        return total
