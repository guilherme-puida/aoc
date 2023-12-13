from aoc.lib.base_solution import BaseSolution

import functools


class Solution(BaseSolution):
    result_one = 7670
    result_two = 157383940585037 

    def setup(self):
        self.entries = []

        for line in self.lines:
            springs, sizes = line.split()
            sizes = [int(x) for x in sizes.split(',')]

            self.entries.append((springs, tuple(sizes)))

    @functools.cache
    def solve(self, springs, sizes, result=0):
        if not sizes:
            return '#' not in springs

        current, rest = sizes[0], sizes[1:]
        for i in range(len(springs) - sum(rest) - len(rest) - current + 1):
            if '#' in springs[:i]:
                break

            next_pos = i + current

            if (
                next_pos <= len(springs)
                and '.' not in springs[i:next_pos]
                and springs[next_pos:next_pos+1] != '#'
            ):
                result += self.solve(springs[next_pos + 1:], rest)

        return result 

    def part_one(self):
        return sum(self.solve(*e) for e in self.entries)

    def part_two(self):
        entries = [
            ('?'.join([springs] * 5), sizes * 5)
            for springs, sizes in self.entries
        ]

        return sum(self.solve(*e) for e in entries)
