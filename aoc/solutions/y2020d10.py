from aoc.lib.base_solution import BaseSolution

import collections
import itertools


class Solution(BaseSolution):
    result_one = 2170
    result_two = 24803586664192

    def setup(self):
        self.numbers = [0] + sorted(int(x) for x in self.lines)
        self.numbers.append(self.numbers[-1] + 3)

    def part_one(self):
        differences = []

        for n1, n2 in itertools.pairwise(self.numbers):
            differences.append(n2 - n1)

        counter = collections.Counter(differences)
        return counter[1] * counter[3]

    def part_two(self):
        paths = collections.defaultdict(int)
        paths[0] = 1

        for n in self.numbers[1:]:
            paths[n] = paths[n - 3] + paths[n - 2] + paths[n - 1]

        return paths[self.numbers[-1]]
