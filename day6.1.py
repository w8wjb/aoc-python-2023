#!/usr/bin/env python3.11

import sys
import re
from math import sqrt, ceil, floor

filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

times = re.split("\s+", lines[0])
times = [int(n) for n in times[1:]]
distances = re.split("\s+", lines[1])
distances = [int(n) for n in distances[1:]]

ways_to_win = 1

for time, distance in zip(times, distances):
    x1 = (time - sqrt(pow(time, 2) - (4 * distance))) / 2
    x2 = (time + sqrt(pow(time, 2) - (4 * distance))) / 2
    span = ceil(x2) - floor(x1) - 1

    ways_to_win *= span

print(ways_to_win)
