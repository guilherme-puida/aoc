from aoc.lib.base_solution import BaseSolution

import collections


def get_hand_type(hand):
    counter = collections.Counter(hand)
    if len(counter) == 1:
        return 6

    (_, hi), (_, lo) = counter.most_common(2)
    return [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1)].index((hi, lo))

def get_hand_type_joker(hand):
    if "J" not in hand:
        return get_hand_type(hand)

    counter = collections.Counter(hand)
    joker_count = counter["J"]
    del counter["J"]

    if not counter or len(counter) == 1:
        return 6

    (_, hi), (_, lo) = counter.most_common(2)
    hi += joker_count

    return [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1)].index((hi, lo))


class Solution(BaseSolution):
    result_one = 249204891 
    result_two = 249666369 

    def setup(self):
        self.hands = []

        for line in self.lines:
            cards, bid = line.split()
            self.hands.append((cards, int(bid)))

    def solve(self, card_order, hand_type_fn):
        entries = []

        for cards, bid in self.hands:
            hand_type = hand_type_fn(cards)
            counter = collections.Counter(cards)
            card_values = [card_order.index(x) for x in cards]
            entry = (bid, (hand_type, *card_values))
            entries.append(entry)

        entries = sorted(entries, key=lambda x: x[1])

        return sum(
            (i + 1) * bid for i, (bid, _) in enumerate(entries)
        )

    def part_one(self):
        return self.solve("23456789TJQKA", get_hand_type)

    def part_two(self):
        return self.solve("J23456789TQKA", get_hand_type_joker)
