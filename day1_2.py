#!/usr/bin/env python3.11

import sys

filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

lines.append("") # Add one extra blank line so that the last elf gets processed

calorie_sum = 0
elves = []

for line in lines:
    if line:
        calories = int(line)
        calorie_sum += calories
    else:
        elves.append(calorie_sum)
        calorie_sum = 0

elves.sort(reverse=True)

print(sum(elves[:3]))
