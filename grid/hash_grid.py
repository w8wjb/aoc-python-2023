"""HashGrid represents a grid of objects using a map keyed by a points"""
from typing import List
from .point import Point


class HashGrid(object):

    def __init__(
        self,
        initialPoints: dict[Point, any] | None = None,
        rows: List[str] | None = None,
    ) -> None:
        self.points = {}
        self.minX = 0
        self.minY = 0
        self.maxX = 0
        self.maxY = 0
        if initialPoints:
            for k, v in initialPoints:
                self[k] = v
        
        if rows:
            for y, row in enumerate(rows):
                for x, c in enumerate(row):
                    if c == '.':
                        continue
                    p = Point(x, y)
                    self[p] = c

    def __setitem__(self, p, val):
        if isinstance(p, (List, tuple)):
            p = Point(p[0], p[1])

        self.minX = min(p.x, self.minX)
        self.minY = min(p.y, self.minY)
        self.maxX = max(p.x, self.maxX)
        self.maxY = max(p.y, self.maxY)
        self.points[p] = val

    def __getitem__(self, p) -> str:
        if isinstance(p, (List, tuple)):
            return self.points[Point(p[0], p[1])]
        return self.points[p]

    def __repr__(self) -> str:
        output = ""
        for y in range(self.minY, self.maxY + 1):            
            for x in range(self.minX, self.maxX + 1):
                output += self.points.get(Point(x, y), '.')
            output += "\n"
        return output