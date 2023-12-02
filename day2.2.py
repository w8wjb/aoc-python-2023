#!/usr/bin/env python3.11

import sys

game_id_sum = 0
filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

power_sum = 0

for line in lines:

    game_header, round_list = line.split(":", 2)
    game_id = int(game_header.removeprefix("Game "))

    rounds = [r.strip() for r in round_list.split(";")]

    color_max = {"red":1, "green":1, "blue":1}

    for round in rounds:
        pairs = [p.strip() for p in round.split(",")]
        for pair in pairs:
            cubes, color = pair.split(" ", 2)
            cubes = int(cubes)
            color_max[color] = max(color_max[color], cubes)

    power = color_max["red"] * color_max["green"] * color_max["blue"]
    power_sum += power

print(power_sum)
