from aoc.lib.base_solution import BaseSolution

import itertools
import re


path_regex = re.compile(r"(\w+) to (\w+) = (\d+)")


class Solution(BaseSolution):
    def setup(self):
        graph = {}
        cities = set()

        for line in self.lines:
            start, end, distance = path_regex.match(line).groups()
            cities.add(start)
            cities.add(end)
            graph[start, end] = int(distance)
            graph[end, start] = int(distance)

        permutations = itertools.permutations(cities)

        self.distances = []
        for permutation in permutations:
            permutation_distance = 0
            for start, end in itertools.pairwise(permutation):
                permutation_distance += graph[start, end]
            self.distances.append(permutation_distance)

    def part_one(self):
        return min(self.distances)

    def part_two(self):
        return max(self.distances)
