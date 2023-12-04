from aoc.lib.base_solution import BaseSolution

import collections
import re


command_regex = re.compile(r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)")


class Solution(BaseSolution):
    result_one = 377891
    result_two = 14110788

    def setup(self):
        self.commands = []
        for line in self.lines:
            command, *pos = command_regex.match(line).groups()
            self.commands.append((command, *map(int, pos)))

    def part_one(self):
        fns = {
            "turn on": lambda _: 1,
            "turn off": lambda _: 0,
            "toggle": lambda x: 0 if x else 1
        }

        return self.solve(fns)


    def part_two(self):
        fns = {
            "turn on": lambda x: x + 1,
            "turn off": lambda x: max(x - 1, 0),
            "toggle": lambda x: x + 2,
        }

        return self.solve(fns)

    def solve(self, fns):
        grid = collections.defaultdict(int)

        for command, *pos in self.commands:
            square = self.get_square(*pos)
            fn = fns[command]

            for p in square:
                grid[p] = fn(grid[p])

        return sum(grid.values())


    def get_square(self, x0, y0, x1, y1):
        positions = []

        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                positions.append((x, y))

        return positions
