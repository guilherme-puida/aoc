from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    result_one = 28651
    result_two = 25450

    def setup(self):
        self.patterns = self.input_str.split("\n\n")

    def solve(self, pattern, diff):
        lines = pattern.splitlines()
        transposed = list(map(list, zip(*lines)))

        def reflection(pat):
            for i in range(1, len(pat)):
                above, below = pat[:i], pat[i:]
                matches = list(zip(reversed(above), below))

                diffs = 0

                for x, y in matches:
                    diffs += sum(a != b for a, b in zip(x, y))

                if diffs == diff:
                    return i

            return 0

        return reflection(transposed) + 100 * reflection(lines)

    def part_one(self):
        return sum(self.solve(p, 0) for p in self.patterns)

    def part_two(self):
        return sum(self.solve(p, 1) for p in self.patterns)
