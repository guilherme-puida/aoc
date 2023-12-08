from aoc.lib.base_solution import BaseSolution

import itertools
import math
import re


class Solution(BaseSolution):
    result_one = 12083
    result_two = 13385272668829

    def setup(self):
        directions, maps = self.input_str.split("\n\n")

        self.directions = [0 if d == "L" else 1 for d in directions]

        self.maps = {}

        for m in maps.splitlines():
            start, left, right = re.match(r"(\w+) = \((\w+), (\w+)\)", m).groups()
            self.maps[start] = (left, right)

    def part_one(self):
        return self.solve(lambda x: x == "AAA", lambda x: x == "ZZZ")

    def part_two(self):
        return self.solve(lambda x: x.endswith("A"), lambda x: x.endswith("Z"))

    def solve(self, start_fn, end_fn):
        cur = [c for c in self.maps.keys() if start_fn(c)]

        result = []

        for c in cur:
            steps = 0

            for e in itertools.cycle(self.directions):
                steps += 1
                c = self.maps[c][e]

                if end_fn(c):
                    result.append(steps)
                    break

        return math.lcm(*result)
