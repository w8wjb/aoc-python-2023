#!/usr/bin/env python3.11

import sys
import re
import numpy as np
from typing import List


filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

regex_edges = re.compile(r"^(\w+)\s+=\s+\((\w+),\s+(\w+)\)")

path = lines.pop(0)
lines.pop(0)

nodes: dict[str, tuple] = {}

for line in lines:
    nid, left, right = regex_edges.match(line).groups()
    nodes[nid] = (left, right)

starting = [n for n in nodes.keys() if n.endswith("A")]
step_counts: List[int] = []

for current in starting:
    steps = 0
    while not current.endswith("Z"):
        fork = nodes[current]
        choose = path[steps % len(path)]
        if choose == "L":
            current = fork[0]
        else:
            current = fork[1]
        steps += 1
    step_counts.append(steps)

print(np.lcm.reduce(step_counts))
