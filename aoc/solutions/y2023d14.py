from aoc.lib.base_solution import BaseSolution


class Solution(BaseSolution):
    result_one = 109596
    result_two = 96105

    def setup(self):
        self.rocks = set()
        self.positions = set()

        for row, line in enumerate(self.lines):
            for col, el in enumerate(line):
                pos = (row, col)
                if el == 'O':
                    self.rocks.add(pos)
                    self.positions.add(pos)
                elif el == '.':
                    self.positions.add(pos)

        self.width = len(self.lines[0])
        self.height = len(self.lines)

    def tilt(self, rocks, direction):
        return self._tilt(tuple(rocks), direction)

    def _tilt(self, rocks, direction):
        rocks = set(rocks)
        row_off, col_off = direction

        while True:
            changed = False

            for row, col in rocks:
                next_pos = (row + row_off, col + col_off)
                if next_pos in self.positions and next_pos not in rocks:
                    rocks.add(next_pos)
                    rocks.remove((row, col))
                    changed = True

            if not changed:
                break

        return rocks

    def part_one(self):
        rocks = self.tilt(self.rocks.copy(), (-1, 0))
        return sum(self.height - row for row, _ in rocks)

    def part_two(self):
        rocks = self.rocks.copy()
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        seen = set()

        i = 0
        while True:
            i += 1
            for d in directions:
                rocks = self.tilt(rocks, d)

            t_rocks = tuple(rocks)
            if t_rocks in seen:
                break

            seen.add(t_rocks)

        cycle = [rocks.copy()]
        while True:
            for d in directions:
                rocks = self.tilt(rocks, d)

            if rocks == cycle[0]:
                break

            cycle.append(rocks.copy())
        
        final = cycle[(1_000_000_000 - i) % len(cycle)]
        return sum(self.height - row for row, _ in final)
