#!/usr/bin/env python3.11

import sys


filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

for line in lines:
    pass

steps = 0
print(steps)
