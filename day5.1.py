#!/usr/bin/env python3.11

import sys
from typing import List


filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

class RangeShift:
    def __init__(self, dest_start:int, src_start:int, range_len:int) -> None:
        self.src = range(src_start, src_start + range_len)
        self.offset = dest_start - src_start

    def __repr__(self) -> str:
        return f"{self.src} -> {self.offset}"
    
    # this exists to make this class act like a range object because I can't subclass it
    def __contains__(self, __key: object):
        return self.src.__contains__(__key)

seeds: List[int] = []
steps: List[List[RangeShift]] = []
shifts: List[RangeShift] = []

for line in lines:
    if not line:
        continue
    
    if line.startswith('seeds'):
        nums = line.removeprefix("seeds: ")
        seeds = [int(n) for n in nums.split()]
    elif line[0].isdigit():
        dest_start, src_start, range_len = [int(n) for n in line.split()]
        shifts.append(RangeShift(dest_start, src_start, range_len))
    else:
        shifts = []
        steps.append(shifts)


for step in steps:
    tmp_seeds = seeds
    for i, seed in enumerate(tmp_seeds):
        for shift in step:
            if seed in shift:
                seeds[i] = seed + shift.offset
    
print(min(seeds))
