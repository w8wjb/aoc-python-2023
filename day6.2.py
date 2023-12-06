#!/usr/bin/env python3.11

import sys
from math import sqrt, ceil, floor

filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

time = int(lines[0].removeprefix('Time:').replace(' ', ''))
distance = int(lines[1].removeprefix('Distance:').replace(' ', ''))

x1 = (time - sqrt(pow(time, 2) - (4 * distance))) / 2
x2 = (time + sqrt(pow(time, 2) - (4 * distance))) / 2
span = ceil(x2) - floor(x1) - 1

print(span)
