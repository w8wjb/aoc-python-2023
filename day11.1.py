#!/usr/bin/env python3.11

import sys
from typing import List

from grid import HashGrid, Point


def expand_universe(lines: List[str], distance:int) -> HashGrid:

    universe = HashGrid()

    empty_rows = set(range(0, len(lines)))
    empty_cols = set(range(0, len(lines[0])))

    for y, row in enumerate(input):
        for x, c in enumerate(row):
            if c != '.':
                p = Point(x, y)
                universe[p] = c
                empty_rows.remove(y)
                empty_cols.remove(x)

    expanded_universe = HashGrid()

    for p, val in universe.points:
        dx = 0
        for col_x in empty_cols:
            if col_x < p.x:
                dx += distance

        dy = 0
        for row_y in empty_rows:
            if row_y < p.y:
                dy += distance

        p2 = p + (dx, dy)
        expanded_universe[p2] = val


    return expanded_universe


def main(file_input, distance:int):

    input_lines = [line.rstrip() for line in file_input]
    universe = expand_universe(input_lines, distance)

    steps = 0
    print(steps)
    

if __name__ == "__main__":
    filename = sys.argv[1]
    distance = int(sys.argv[1]) - 1
    
    with open(filename, encoding="utf-8") as file:
        main(file, distance)
