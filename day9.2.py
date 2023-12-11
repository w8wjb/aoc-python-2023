#!/usr/bin/env python3.11

import sys
from itertools import pairwise

filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]


def all_zeros(sequence: list[int]) -> bool:
    for n in sequence:
        if n != 0:
            return False
    return True


def predict(sequence: list[int], end: bool) -> int:
    if all_zeros(sequence):
        return 0

    subsequence = [y - x for (x, y) in pairwise(sequence)]
    prediction = predict(subsequence, end)
    if end:
        return sequence[-1] + prediction

    return sequence[0] - prediction


sum_prediction = 0
for line in lines:
    history = [int(n) for n in line.split()]
    sum_prediction += predict(history, False)

print(sum_prediction)
