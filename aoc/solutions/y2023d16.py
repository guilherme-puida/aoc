from aoc.lib.base_solution import BaseSolution
from aoc.lib.space import Direction, Point


class Solution(BaseSolution):
    result_one = 7728
    result_two = 8061

    def setup(self):
        self.width = len(self.lines[0])
        self.height = len(self.lines)

    def solve(self, origin, direction):
        beams = [(origin, direction)]
        visited = set()

        for i, (point, direction) in enumerate(beams):
            while 0 <= point.x < self.width and 0 <= point.y < self.height:
                if (point, direction) in visited:
                    break

                visited.add((point, direction))
                current = self.lines[point.y][point.x]
                match (current, direction):
                    case ("\\", Direction.EAST):
                        direction = Direction.NORTH
                    case ("\\", Direction.WEST):
                        direction = Direction.SOUTH
                    case ("\\", Direction.SOUTH):
                        direction = Direction.WEST
                    case ("\\", Direction.NORTH):
                        direction = Direction.EAST
                    case ("/", Direction.EAST):
                        direction = Direction.SOUTH
                    case ("/", Direction.WEST):
                        direction = Direction.NORTH
                    case ("/", Direction.SOUTH):
                        direction = Direction.EAST
                    case ("/", Direction.NORTH):
                        direction = Direction.WEST
                    case ("-", Direction.NORTH | Direction.SOUTH):
                        east = (point, Direction.EAST)
                        west = (point, Direction.WEST)
                        beams.append(east)
                        beams.append(west)
                        break
                    case ("|", Direction.EAST | Direction.WEST):
                        north = (point, Direction.NORTH)
                        south = (point, Direction.SOUTH)
                        beams.append(north)
                        beams.append(south)
                        break

                point = point.move(direction)

        return len(set(point for point, _ in visited))

    def part_one(self):
        return self.solve(Point.origin(), Direction.EAST)
        
    def part_two(self):
        west_edge = [(Point(0, y), Direction.EAST) for y in range(self.height)]
        east_edge = [(Point(self.width, y), Direction.WEST) for y in range(self.height)]
        north_edge = [(Point(x, 0), Direction.SOUTH) for x in range(self.width)]
        south_edge = [(Point(x, self.height), Direction.NORTH) for x in range(self.width)]

        return max(self.solve(*c) for c in west_edge + east_edge + north_edge + south_edge)
