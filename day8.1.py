#!/usr/bin/env python3.11

import sys
import re
from typing import List


filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

regex_edges = re.compile(r"^(\w+)\s+=\s+\((\w+),\s+(\w+)\)")

path = lines.pop(0)
lines.pop(0)

nodes = {}

for line in lines:
    nid, left, right = regex_edges.match(line).groups()
    nodes[nid] = (left, right)

current = "AAA"

steps = 0
while current != "ZZZ":
    fork = nodes[current]
    choose = path[steps % len(path)]
    if choose == "L":
        current = fork[0]
    else:
        current = fork[1]
    steps += 1

print(steps)
