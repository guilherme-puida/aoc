from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    result_one = 1806615041
    result_two = 1211
    
    def setup(self):
        self.numbers = [[int(x) for x in line.split()] for line in self.lines]

    def part_one(self):
        total = 0

        for line in self.numbers:
            diffs = [line.copy()]

            while not all(x == 0 for x in diffs[-1]):
                new_diffs = []
                for i in range(1, len(diffs[-1])):
                    new_diffs.append(diffs[-1][i] - diffs[-1][i - 1])

                diffs.append(new_diffs)

            diffs[-1].append(0)
            diffs.reverse()

            for i, e in enumerate(diffs[1:]):
                e.append(e[-1] + diffs[i][-1])

            total += diffs[-1][-1]

        return total

    def part_two(self):
        total = 0

        for line in self.numbers:
            diffs = [line.copy()]

            while not all(x == 0 for x in diffs[-1]):
                new_diffs = []

                for i in range(1, len(diffs[-1])):
                    new_diffs.append(diffs[-1][i] - diffs[-1][i - 1])

                diffs.append(new_diffs)

            diffs[-1].insert(0, 0)
            diffs.reverse()

            for i, e in enumerate(diffs[1:]):
                e.insert(0, e[0] - diffs[i][0])

            total += diffs[-1][0]

        return total
