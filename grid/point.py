from typing import List, Tuple


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def inverted(self):
        return Vector(-self.x, -self.y)

    def __repr__(self) -> str:
        return f"{self.x},{self.y}"

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


Vector.NW = Vector(-1, -1)
Vector.N = Vector(0, -1)
Vector.NE = Vector(1, -1)
Vector.W = Vector(-1, 0)
Vector.E = Vector(1, 0)
Vector.SW = Vector(-1, 1)
Vector.S = Vector(0, 1)
Vector.SE = Vector(1, 1)

Vector.ADJACENT_MOVES = (
    Vector.N,
    Vector.NE,
    Vector.E,
    Vector.SE,
    Vector.S,
    Vector.SW,
    Vector.W,
    Vector.NW,
)


class Point(Vector):
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        if isinstance(other, (List, Tuple)):
            return Point(self.x + other[0], self.y + other[1])
        raise f"attempt to add an inappropriate value {other}"

    def __sub__(self, other):
        if isinstance(other, object):
            return Point(self.x - other.x, self.y - other.y)
        if isinstance(other, (List, Tuple)):
            return Point(self.x - other[0], self.y - other[1])
        raise f"attempt to subtract an inappropriate value {other}"

    def __gt__(self, other: "Point") -> bool:
        return (self.x, self.y) > (other.x, other.y)

    def __lt__(self, other: "Point") -> bool:
        return (self.x, self.y) < (other.x, other.y)
