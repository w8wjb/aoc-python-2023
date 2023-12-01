#!/usr/bin/env python3.11

import sys

calorie_sum = 0
filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

calibration_sum = 0

for line in lines:
    numbers = [n for n in line if n.isdigit()]
    calibration = numbers[0] + numbers[-1]
    calibration_sum += int(calibration)

print(calibration_sum)
