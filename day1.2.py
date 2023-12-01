#!/usr/bin/env python3.11

import sys

calorie_sum = 0
filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]
    

digits = [str(n) for n in range(0, 10)]
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
symbols = digits + words

calibration_sum = 0

for line in lines:

    first_index = len(line)
    first_symbol = None
    last_index = -1
    last_symbol = None

    for symbol in symbols:
        i = line.find(symbol)
        if i > -1 and i < first_index:
            first_index = i
            first_symbol = symbol

        j = line.rfind(symbol)
        if j > -1 and j > last_index:
            last_index = j
            last_symbol = symbol

    if not first_symbol.isdigit():
        first_symbol = str(words.index(first_symbol))
    
    if not last_symbol.isdigit():
        last_symbol = str(words.index(last_symbol))


    calibration = first_symbol + last_symbol
    calibration_sum += int(calibration)

print(calibration_sum)
