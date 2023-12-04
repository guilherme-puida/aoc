from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    result_one = 1606483
    result_two = 3842356

    def setup(self):
        self.dimensions = [tuple(map(int, line.split("x"))) for line in self.lines]

    def part_one(self):
        total = 0

        for l, w, h in self.dimensions:
            lw = l * w
            wh = w * h
            hl = h * l

            total += 2 * lw + 2 * wh + 2 * hl + min(lw, wh, hl)

        return total

    def part_two(self):
        total = 0

        for l, w, h in self.dimensions:
            volume = l * w * h
            s1, s2, _ = sorted([l, w, h])

            total += 2 * s1 + 2 * s2 + volume

        return total
