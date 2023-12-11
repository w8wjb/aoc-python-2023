#!/usr/bin/env python3.11
import sys

from typing import Set
from grid import StringGrid, Point, Vector


filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]


class PipeMap(StringGrid):
    def find_start(self) -> Point:
        for p, val in self:
            if val == "S":
                return p
        raise LookupError("Start not found")

    def find_exit(self, p: Point, visited: Set[Point]) -> Point | None:
        for rel_dir in grid.list_avail_directions(p):
            dest = p + rel_dir
            if dest not in visited:
                return dest
        return None

    def list_avail_directions(self, p: Point) -> list[Vector]:
        pipe = self[p]
        if pipe == "|":
            return (Vector.N, Vector.S)
        elif pipe == "-":
            return (Vector.E, Vector.W)
        elif pipe == "L":
            return (Vector.N, Vector.E)
        elif pipe == "J":
            return (Vector.N, Vector.W)
        elif pipe == "7":
            return (Vector.S, Vector.W)
        elif pipe == "F":
            return (Vector.S, Vector.E)
        elif pipe == "S":
            available = []
            for check in (Vector.N, Vector.E, Vector.S, Vector.W):
                neighbor = p + check
                neighbor_dirs = self.list_avail_directions(neighbor)
                if check.inverted() in neighbor_dirs:
                    available.append(check)
            return available

        else:
            return tuple()


grid = PipeMap(rows=lines)

start = grid.find_start()

visited = set([start])

available_dirs = grid.list_avail_directions(start)

current = start + available_dirs[0]

while True:
    visited.add(current)
    next_tile = grid.find_exit(current, visited)
    if not next_tile:
        break
    current = next_tile


contained_points = 0

for y in range(grid.minY, grid.maxY + 1):

    path_count = 0
    last_corner = '.'

    for x in range(grid.minX, grid.maxX + 1):
        p = Point(x, y)

        c = grid[p]

        if p in visited:
            if c in ('S', 'F', 'L'):
                path_count += 1
                last_corner = c
            elif c == 'J':
                if last_corner == 'F':
                    last_corner = c
                else:
                    path_count += 1
                    last_corner = '.'
            elif c == '7':
                if last_corner == 'L':
                    last_corner = c
                else:
                    path_count += 1
                    last_corner = '.'

            if c != '-':
                path_count += 1
        else:
            if (path_count % 2) == 1:
                contained_points += 1

print(contained_points)
