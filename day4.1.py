#!/usr/bin/env python3.11

import sys
import re


filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]


regex_game_parts = re.compile(r"Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)")

deck_score = 0

for line in lines:
    card_id, winning_section, scratched_section = regex_game_parts.match(line).groups()
    winning_nums = set(re.split('\s+', winning_section))
    scratched = set(re.split('\s+', scratched_section))
    match_count = len(winning_nums & scratched)
    if match_count > 0:
        points = pow(2, match_count - 1)
        deck_score += points

print(deck_score)
