from aoc.lib.base_solution import BaseSolution

import json


class Solution(BaseSolution):
    def setup(self):
        self.json = json.loads(self.input_str)

    def part_one(self):
        return self.solve(self.json)

    def part_two(self):
        return self.solve(self.json, True)

    def solve(self, node, ignore_red=False):
        if isinstance(node, int):
            return node

        if isinstance(node, list):
            return sum(self.solve(x, ignore_red) for x in node)

        if isinstance(node, dict):
            if ignore_red and "red" in node.values():
                return 0

            return sum(self.solve(x, ignore_red) for x in node.values())

        return 0
