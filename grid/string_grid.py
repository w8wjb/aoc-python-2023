"""StringGrid represents a grid of characters using a list of strings"""
from typing import List
from .point import Point


        
class StringGrid(object):
    def __init__(self, rows: List[str]) -> None:
        self.rows = rows
        self.minY = 0
        self.minX = 0
        self.maxY = len(rows) - 1
        self.maxX = len(rows[0]) - 1

    def __getitem__(self, p) -> str:
        if isinstance(p, Point):
            x = p.x
            y = p.y
        elif isinstance(p, (List, tuple)):
            x = p[0]
            y = p[1]
        else:
            raise "Unexpected index object: " + p

        if x < self.minX or y < self.minY or x > self.maxX or y > self.maxY:
            return "."
        return self.rows[y][x]

    def __repr__(self) -> str:
        return "\n".join(self.rows)
    

    def __iter__(self):
        class StringGridItor:
            def __init__(self, grid:"StringGrid") -> None:
                self.grid = grid
                self.x = grid.minX
                self.y = grid.minY

            def __next__(self):
                if self.y > self.grid.maxY:
                    raise StopIteration()
                p = Point(self.x, self.y)
                value = self.grid[p]

                self.x += 1
                if self.x > self.grid.maxX:
                    self.x = 0
                    self.y += 1
                return (p, value)

        return StringGridItor(self)
    



