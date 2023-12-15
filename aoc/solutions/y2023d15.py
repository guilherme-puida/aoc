from aoc.lib.base_solution import BaseSolution

import collections


class Solution(BaseSolution):
    result_ont = 515495
    result_two = 229349

    def setup(self):
        self.ops = self.input_str.split(",")

    def hash(self, string):
        h = 0

        for c in string:
            h += ord(c)
            h *= 17
            h %= 256

        return h

    def part_one(self):
        return sum(self.hash(op) for op in self.ops)

    def part_two(self):
        boxes = collections.defaultdict(list)

        def find(box, label):
            for i, (l, _) in enumerate(box):
                if l == label:
                    return i

            return None

        for op in self.ops:
            if "=" in op:
                label, value = op.split("=")
                box = boxes[self.hash(label)]
                el = (label, int(value))
                i = find(box, label)

                if i is not None:
                    box[i] = el
                else:
                    box.append(el)
            else:
                label = op.rstrip("-")
                box = boxes[self.hash(label)]
                i = find(box, label)

                if i is not None:
                    box.pop(i)

        total = 0
        for box, values in boxes.items():
            for i, (_, value) in enumerate(values):
                total += (box + 1) * (i + 1) * value

        return total
