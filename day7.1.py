#!/usr/bin/env python3.11

from functools import cmp_to_key
import sys

filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]


class Hand:
    def __init__(self, hand_str: str) -> None:
        parts = hand_str.split(" ")
        self.cards = parts[0]
        self.bid = int(parts[1])

    def hand_type(self) -> int:
        char_count = {" ": 0}
        for c in self.cards:
            char_count[c] = char_count.get(c, 0) + 1

        freqs = list(char_count.values())
        freqs.sort(reverse=True)
        primary_count = freqs[0]
        secondary_count = freqs[1]

        hand_type = 0
        if primary_count == 5:  # Five of a kind
            hand_type = 6
        elif primary_count == 4:  # Four of a kind
            hand_type = 5
        elif primary_count == 3 and secondary_count == 2:  # Full house
            hand_type = 4
        elif primary_count == 3:  # Three of a kind
            hand_type = 3
        elif primary_count == 2 and secondary_count == 2:  # Two pair
            hand_type = 2
        elif primary_count == 2:  # One pair
            hand_type = 1
        return hand_type

    def __repr__(self) -> str:
        return self.cards


hands = list(map(Hand, lines))

card_order = "23456789TJQKA"


def card_compare(a: Hand, b: Hand):
    a_hand_type = a.hand_type()
    b_hand_type = b.hand_type()
    if a_hand_type == b_hand_type:
        for ac, bc in zip(a.cards, b.cards):
            if ac == bc:
                continue
            return card_order.index(ac) - card_order.index(bc)
        return 0
    else:
        return a_hand_type - b_hand_type


hands.sort(key=cmp_to_key(card_compare))

total_winnings = 0
for i, hand in enumerate(hands):
    winnings = hand.bid * (i + 1)
    total_winnings += winnings

print(total_winnings)
