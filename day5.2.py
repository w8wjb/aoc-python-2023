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

seeds: List[range] = []
steps: List[List[RangeShift]] = []
shifts: List[RangeShift] = []

for line in lines:
    if not line:
        continue
    
    if line.startswith('seeds'):
        line_tmp = line.removeprefix("seeds: ")
        numbers = [int(n) for n in line_tmp.split()]

        for i in range(0, len(numbers), 2):
            start = numbers[i]
            end = start + numbers[i+1]
            seeds.append(range(start, end))

    elif line[0].isdigit():
        dest_start, src_start, range_len = [int(n) for n in line.split()]
        shifts.append(RangeShift(dest_start, src_start, range_len))
    else:
        shifts = []
        steps.append(shifts)


for step in steps:

    i = 0
    while i < len(seeds):
        seed_range = seeds[i]

        for shift in step:
            if seed_range.start in shift:
                if seed_range.stop > shift.src.stop:

                    smaller_range = range(seed_range.start, shift.src.stop)
                    remainder_range = range(smaller_range.stop, seed_range.stop)
                    seeds.append(remainder_range)

                    seed_range = smaller_range
                
                seeds[i] = range(seed_range.start + shift.offset, 
                                 seed_range.stop + shift.offset)
                break

        i += 1

    
print(min([s.start for s in seeds]))
