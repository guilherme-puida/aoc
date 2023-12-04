import dataclasses
import enum

from typing import Self


class Direction(enum.Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def to_offset(self) -> tuple[int, int]:
        """Returns the offset (x, y) associated with a given Direction."""
        match self:
            case Direction.NORTH:
                return (0, 1)
            case Direction.EAST:
                return (1, 0)
            case Direction.SOUTH:
                return (0, -1)
            case Direction.WEST:
                return (-1, 0)


@dataclasses.dataclass(frozen=True)
class Point:
    x: int
    y: int

    @classmethod
    def origin(cls):
        return cls(0, 0)

    def move(self, direction: Direction) -> Self:
        x_off, y_off = direction.to_offset()
        return Point(self.x + x_off, self.y + y_off)
        
