from aoc.lib.base_solution import BaseSolution

import collections


class Solution(BaseSolution):
    result_one = 21138
    result_two = 7185540

    def setup(self):
        self.cards = []

        for line in self.lines:
            winning, mine = line.split(" | ")
            winning = winning.split(": ")[1]
            winning = set(map(int, winning.split()))
            mine = set(map(int, mine.split()))
            both = winning & mine
            self.cards.append(both)

    def part_one(self):
        total = 0

        for both in self.cards:
            if not both:
                continue

            total += 2 ** (len(both) - 1)

        return total

    def part_two(self):
        cards = collections.defaultdict(lambda: 1)

        for i, both in enumerate(self.cards):
            i = i + 1
            cur = cards[i]
            for c in range(i + 1, i + len(both) + 1):
                cards[c] += cur

        return sum(cards.values())
