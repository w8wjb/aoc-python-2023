#!/usr/bin/env python3.11

import sys

game_id_sum = 0
filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

calibration_sum = 0

red_limit = 12
green_limit = 13
blue_limit = 14

for line in lines:

    game_header, round_list = line.split(":", 2)
    game_id = int(game_header.removeprefix("Game "))
    game_valid = True

    rounds = [r.strip() for r in round_list.split(";")]

    for round in rounds:
        if not game_valid:
            break
        pairs = [p.strip() for p in round.split(",")]
        for pair in pairs:
            cubes, color = pair.split(" ", 2)
            cubes = int(cubes)
            if color == "red" and cubes > red_limit:
                game_valid = False
                break
            elif color == "green" and cubes > green_limit:
                game_valid = False
                break
            elif color == "blue" and cubes > blue_limit:
                game_valid = False
                break

    if game_valid:
        game_id_sum += game_id

print(game_id_sum)
