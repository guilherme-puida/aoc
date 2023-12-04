from aoc.lib.base_solution import BaseSolution

import collections
import itertools
import re


line_regex = re.compile(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)")


class Solution(BaseSolution):
    def setup(self):
        self.graph = collections.defaultdict(int)
        self.people = set()

        for line in self.lines:
            p1, sign, amount, p2 = line_regex.match(line).groups()
            self.people.add(p1)
            self.people.add(p2)

            self.graph[p1, p2] = int(amount) * (1 if sign == "gain" else -1)

    def part_one(self):
        return self.solve(self.people)

    def part_two(self):
        return self.solve(self.people | {"me"})

    def solve(self, people):
        permutations = itertools.permutations(people)
        max_score = 0

        for permutation in permutations:
            score = 0
            for p1, p2 in itertools.pairwise(permutation):
                score += self.graph[p1, p2]
                score += self.graph[p2, p1]

            score += self.graph[permutation[0], permutation[-1]]
            score += self.graph[permutation[-1], permutation[0]]

            max_score = max(max_score, score)

        return max_score
