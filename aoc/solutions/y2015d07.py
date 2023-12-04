from aoc.lib.base_solution import BaseSolution

import functools


class Solution(BaseSolution):
    result_one = 3176
    result_two = 14710

    def setup(self):
        self.data = {}

        for line in self.lines:
            command, dest = line.split(" -> ")
            self.data[dest] = command

    def part_one(self):
        self.result = str(self.evaluate("a"))
        return int(self.result)

    def part_two(self):
        if not self.result:
            self.part_one()

        self.data["b"] = self.result
        self.evaluate.cache_clear()
        return self.evaluate("a")

    @functools.lru_cache
    def evaluate(self, key):
        try:
            return int(key)
        except ValueError:
            pass

        match self.data[key].split():
            case [x]:
                return self.evaluate(x)
            case ["NOT", x]:
                return ~self.evaluate(x)
            case [x, "AND", y]:
                return self.evaluate(x) & self.evaluate(y)
            case [x, "OR", y]:
                return self.evaluate(x) | self.evaluate(y)
            case [x, "LSHIFT", y]:
                return self.evaluate(x) << self.evaluate(y)
            case [x, "RSHIFT", y]:
                return self.evaluate(x) >> self.evaluate(y)
