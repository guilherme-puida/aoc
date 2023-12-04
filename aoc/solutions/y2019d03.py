from aoc.lib.base_solution import BaseSolution
from aoc.lib.space import Direction, Point


def direction_from_char(char: str) -> Direction:
    match char:
        case "U": return Direction.NORTH
        case "R": return Direction.EAST
        case "D": return Direction.SOUTH
        case "L": return Direction.WEST

class Solution(BaseSolution):
    result_one = 865
    result_two = 35038

    def setup(self):
        def parse_instructions(instructions):
            result = []

            for operation in instructions.split(","):
                direction, amount = operation[0], operation[1:]
                result.append((direction_from_char(direction), int(amount)))

            return result

        instructions_a = parse_instructions(self.lines[0])
        instructions_b = parse_instructions(self.lines[1])

        w1 = w2 = origin = Point.origin()
        self.w1_visited = {origin: 0}
        self.w2_visited = {origin: 0}

        for direction, amount in instructions_a:
            for i in range(1, amount + 1):
                current_distance = self.w1_visited[w1]
                w1 = w1.move(direction)
                self.w1_visited[w1] = current_distance + 1

        for direction, amount in instructions_b:
            for i in range(1, amount + 1):
                current_distance = self.w2_visited[w2]
                w2 = w2.move(direction)
                self.w2_visited[w2] = current_distance + 1

        self.common_points = set(self.w1_visited.keys()) & set(self.w2_visited.keys())

    def part_one(self):
        origin = Point.origin()
        return min(origin.manhattan_distance(x) for x in self.common_points if x != origin)

    def part_two(self):
        origin = Point.origin()
        return min(
            self.w1_visited[x] + self.w2_visited[x]
            for x in self.common_points
            if x != origin
        )
