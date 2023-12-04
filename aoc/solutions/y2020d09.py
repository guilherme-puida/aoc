from aoc.lib.base_solution import BaseSolution

import itertools


class Solution(BaseSolution):
    result_one = 22406676
    result_two = 2942387

    def setup(self):
        self.numbers = [int(x) for x in self.lines]

    def part_one(self):
        ns = self.numbers[:25]

        for n in self.numbers[25:]:
            sums = []
            for a, b in itertools.product(ns, ns):
                if a != b:
                    sums.append(a + b)

            if n not in sums:
                return n

            ns = ns[1:] + [n]

    def part_two(self):
        target = self.part_one()

        result = start = 0
        for end, _ in enumerate(self.numbers):
            result += self.numbers[end]

            while target < result:
                result -= self.numbers[start]
                start += 1

            if result == target:
                ns = self.numbers[start:end+1]
                return min(ns) + max(ns)
