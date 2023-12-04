from aoc.lib.base_solution import BaseSolution

import hashlib


class Solution(BaseSolution):
    result_one = 346386
    result_two = 9958218

    def setup(self):
        pass

    def part_one(self):
        return self.solve(5)

    def part_two(self):
        return self.solve(6)

    def solve(self, amount):
        i = 1
        prefix = "0" * amount

        while True:
            digest = hashlib.md5(f"{self.input_str}{i}".encode()).hexdigest()
            if digest.startswith(prefix):
                return i

            i += 1
