from aoc.lib.base_solution import BaseSolution

import re


class Solution(BaseSolution):
    def setup(self):
        self.height = len(self.lines)
        self.width = len(self.lines[0])
        pass

    def part_one(self):
        total = 0

        numbers = re.finditer(r"(\d+)", ''.join(self.lines))

        for number in numbers:
            n_len = len(number.group())
            start, _ = number.span()

            row, col = divmod(start, self.width)

            spots = [
                (row, col + n_len),
                (row, col - 1),
                *[(row - 1, col + c) for c in range(-1, n_len + 1)],
                *[(row + 1, col + c) for c in range(-1, n_len + 1)],
            ]

            if any(self.is_sym(*x) for x in spots):
                total += int(number.group())

        return total

    def part_two(self):
        numbers = {}

        for number in re.finditer(r"(\d+)", ''.join(self.lines)):
            n = number.group()
            for i in range(*number.span()):
                numbers[i] = int(n)

        total = 0

        for gear in re.finditer(r"(\*)", "".join(self.lines)):
            start, _ = gear.span()
            row, col = divmod(start, self.width)

            around = [
                (row - 1, col - 1),
                (row - 1, col),
                (row - 1, col + 1),
                (row, col - 1),
                (row, col + 1),
                (row + 1, col - 1),
                (row + 1, col),
                (row + 1, col + 1),
            ]

            n_around = []
            for nrow, ncol in around:
                if nrow not in range(self.height):
                    continue
                if ncol not in range(self.width):
                    continue

                pp = nrow * self.width + ncol
                if pp in numbers:
                    n_around.append(numbers[pp])

            n_around = list(set(n_around))
            if len(n_around) == 2:
                total += n_around[0] * n_around[1]

        return total

    def is_sym(self, row, col):
        if row not in range(self.height):
            return False
        if col not in range(self.width):
            return False

        c = self.lines[row][col]
        return c not in '.0123456789'
