from aoc.lib.base_solution import BaseSolution

import re


class Solution(BaseSolution):
    result_one = 533784
    result_two = 78826761

    def setup(self):
        self.width = len(self.lines[0])

        self.numbers = {}

        sanitized_input = self.input_str.replace("\n", "")

        for number in re.finditer(r"(\d+)", sanitized_input):
            n = int(number.group())
            start, end = number.span()
            for i in range(start, end):
                self.numbers[i] = (n, start)

        self.symbols = {}

        for sym in re.finditer(r"([^\.0-9])", sanitized_input):
            start, _ = sym.span()
            self.symbols[start] = sym.group()

    def part_one(self):
        numbers = set()

        for start, sym in self.symbols.items():
            row, col = divmod(start, self.width)

            for index in self.around(row, col):
                if index in self.numbers:
                    numbers.add(self.numbers[index])

        return sum(val for val, _ in numbers)

    def part_two(self):
        total = 0

        for start, sym in self.symbols.items():
            if sym != "*":
                continue

            numbers = set()
            row, col = divmod(start, self.width)

            for index in self.around(row, col):
                if index in self.numbers:
                    numbers.add(self.numbers[index])

            if len(numbers) == 2:
                (n1, _), (n2, _) = numbers
                total += n1 * n2

        return total

    def around(self, row, col):
        a = [
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col - 1),
            (row, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1),
        ]

        return [p * self.width + c for p, c in a]
