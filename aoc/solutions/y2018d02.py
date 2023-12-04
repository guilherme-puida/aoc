from aoc.lib.base_solution import BaseSolution

import collections
import itertools


class Solution(BaseSolution):
    def setup(self):
        pass

    def part_one(self):
        twos = 0
        threes = 0

        for line in self.lines:
            counter = collections.Counter(line)
            values = counter.values()

            if 2 in values:
                twos += 1

            if 3 in values:
                threes += 1

        return twos * threes

    def part_two(self):
        for l1, l2 in itertools.product(self.lines, self.lines):
            if l1 == l2:
                continue

            diff = None
            for i, (c1, c2) in enumerate(zip(l1, l2)):
                if c1 != c2:
                    if diff:
                        break

                    diff = i
            else:
                # nasty for-else here. first time i got the chance to use this :^)
                return l1[:diff] + l1[diff+1:]
