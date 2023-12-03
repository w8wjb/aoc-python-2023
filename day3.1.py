#!/usr/bin/env python3.11

import sys

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __hash__(self) -> int:
        return hash((self.x, self.y))
    
    def __eq__(self, other: object) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __repr__(self) -> str:
        return f"{self.x},{self.y}"
    
    def neighbors(self):
        neighbors = set()
        for curr_x in range(self.x - 1, self.x + 2):
            for curr_y in range(self.y - 1, self.y + 2):
                neighbors.add(Point(curr_x, curr_y))
        return neighbors



filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

parts: list[Point] = []
gears: set[Point] = set()
symbols: set[Point] = set()

for y, line in enumerate(lines):

    current_num = 0
    adjacencies = set()

    for x, c in enumerate(line):
        p = Point(x, y)

        if c.isnumeric():            
            adjacencies = adjacencies.union(p.neighbors())            
            current_num = (current_num * 10) + int(c)
        
        else:
            if current_num > 0:
                parts.append((current_num, adjacencies))
                current_num = 0
                adjacencies = set()

            if c == '*':
                gears.add(p)
            
            if c != '.':
                symbols.add(p)

    if current_num > 0:
        parts.append((current_num, adjacencies))

sum_part_nums = 0
for part_num, adjacencies in parts:
    if len(adjacencies & symbols) > 0:
        sum_part_nums += part_num


print(sum_part_nums)
