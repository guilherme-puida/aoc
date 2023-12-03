from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    def part_one(self):
        return self.solve(self.lines)

    def part_two(self):
        new_lines = [
            line.replace("zero", "z0b")
                .replace("one", "o1e")
                .replace("two", "t2o")
                .replace("three", "t3e")
                .replace("four", "f4r")
                .replace("five", "f5e")
                .replace("six", "s6x")
                .replace("seven", "s7n")
                .replace("eight", "e8t")
                .replace("nine", "n9e")
            for line in self.lines
        ]

        return self.solve(new_lines)

    def solve(self, lines: list[str]) -> int:
        total = 0

        for line in lines:
            numbers = [x for x in line if x in "0123456789"]
            total += int(numbers[0] + numbers[-1])

        return total
        
