from aoc.lib.base_solution import BaseSolution
from aoc.lib.space import Point, Direction


class Solution(BaseSolution):
    result_one = 2572
    result_two = 2631

    def setup(self):
        pass

    def part_one(self):
        visited = set()
        santa = Point.origin()
        visited.add(santa)

        for c in self.input_str:
            santa = santa.move(self.direction_from_char(c))
            visited.add(santa)

        return len(visited)

    def part_two(self):
        visited = set()
        santa = robot = Point.origin()
        visited.add(santa)

        for i in range(0, len(self.input_str), 2):
            santa = santa.move(self.direction_from_char(self.input_str[i]))
            robot = robot.move(self.direction_from_char(self.input_str[i + 1]))

            visited.add(santa)
            visited.add(robot)

        return len(visited)

    def direction_from_char(self, c):
        match c:
            case "^": return Direction.NORTH
            case ">": return Direction.EAST
            case "v": return Direction.SOUTH
            case "<": return Direction.WEST
            case _: raise ValueError
