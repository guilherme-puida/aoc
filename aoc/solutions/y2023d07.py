from aoc.lib.base_solution import BaseSolution

import collections


def get_card_value(card):
    return "23456789TJQKA".index(card)

def get_card_value_joker(card):
    return "J23456789TQKA".index(card)

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

    # four of a kind -> five of a kind
    if not counter or len(counter) == 1:
        return 6

    (_, hi), (_, lo) = counter.most_common(2)
    hi += joker_count

    return [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (4, 1)].index((hi, lo))

class Solution(BaseSolution):
    def setup(self):
        self.hands = []

        for line in self.lines:
            cards, bid = line.split()
            self.hands.append((cards, int(bid)))

    def part_one(self):
        sortable_entries = []

        for cards, bid in self.hands:
            hand_type = get_hand_type(cards)
            card_values = [get_card_value(x) for x in cards]
            entry = (bid, (hand_type, *card_values))
            sortable_entries.append(entry)

        entries = sorted(sortable_entries, key=lambda x: x[1])

        total = 0
        for i, (bid, _) in enumerate(entries):
            total += (i + 1) * bid

        return total

    def part_two(self):
        sortable_entries = []

        for cards, bid in self.hands:
            hand_type = get_hand_type_joker(cards)
            card_values = [get_card_value_joker(x) for x in cards]
            entry = (bid, (hand_type, *card_values))
            sortable_entries.append(entry)

        entries = sorted(sortable_entries, key=lambda x: x[1])

        total = 0
        for i, (bid, _) in enumerate(entries):
            total += (i + 1) * bid

        return total
