from aoc.lib.base_solution import BaseSolution

import re


game_regex = r"(\d+) (blue|red|green)"

max_amount = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

class Solution(BaseSolution):
    def part_one(self):
        total = 0

        for i, line in enumerate(self.lines):
            line_ok = all(
                int(amount) <= max_amount[color]
                for amount, color
                in re.findall(game_regex, line)
            )

            if line_ok:
                total += i + 1

        return total

    def part_two(self):
        total = 0

        for line in self.lines:
            power = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }

            for amount, color in re.findall(game_regex, line):
                power[color] = max(power[color], int(amount))

            total += power["red"] * power["green"] * power["blue"]

        return total
