from aoc.lib.base_solution import BaseSolution

import collections


class Solution(BaseSolution):
    def setup(self):
        self.graph = collections.defaultdict(set)
        self.start = None

        self.width = len(self.lines[0])
        self.height = len(self.lines)

        def add_edge(p1, p2):
            if p2[0] not in range(self.height) or p2[1] not in range(self.width):
                return

            self.graph[p1].add(p2)
            self.graph[p2].add(p1)

        def get_element(pos):
            row, col = pos
            if row not in range(self.height) or col not in range(self.width):
                return "."

            return self.lines[row][col]

        for row, line in enumerate(self.lines):
            for col, el in enumerate(line):
                if el == ".":
                    continue

                pos = (row, col)
                north = (row - 1, col)
                east = (row, col + 1)
                south = (row + 1, col)
                west = (row, col - 1)

                connection = {
                    "|": (north, south),
                    "-": (east, west),
                    "L": (north, east),
                    "J": (north, west),
                    "7": (south, west),
                    "F": (south, east),
                    north: "|7F",
                    east: "-J7",
                    south: "|LJ",
                    west: "-LF",
                }

                if el in connection:
                    c1, c2 = connection[el]

                    if get_element(c1) in connection[c1]:
                        add_edge(pos, c1)

                    if get_element(c2) in connection[c2]:
                        add_edge(pos, c2)

                    continue

                # handling start position
                self.start = pos
                adjacent = []

                for a_pos in (north, east, south, west):
                    if get_element(a_pos) in connection[a_pos]:
                        adjacent.append(a_pos)

                c1, c2 = adjacent
                add_edge(pos, c1)
                add_edge(pos, c2)

                self.is_start_vertical = c1 == south or c2 == south 

    def get_path(self):
        visited = {self.start}
        queue = [self.start]

        while queue:
            current = queue.pop(0)
            for el in self.graph[current]:
                if el in visited:
                    continue

                queue.append(el)
                visited.add(el)

        return visited

    def part_one(self):
        return len(self.get_path()) // 2

    def part_two(self):
        visited = self.get_path()
        total = 0

        for row in range(self.height):
            inside = False

            for col in range(self.width):
                pos = (row, col)
                el = self.lines[row][col]
                if pos in visited:
                    if el in "|7F" or (pos == self.start and self.is_start_vertical):
                        inside = not inside
                elif inside:
                    total += 1

        return total
