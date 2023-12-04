#!/usr/bin/env python3.11

import sys
import re


filename = sys.argv[1]

with open(filename, encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

class Card:

    regex_game_parts = re.compile(r"Card\s+(\d+):\s+([\d\s]+)\s+\|\s+([\d\s]+)")

    def __init__(self, line) -> None:
        self.card_id, winning_section, scratched_section = Card.regex_game_parts.match(line).groups()
        self.winning_nums = set(re.split('\s+', winning_section))
        self.scratched = set(re.split('\s+', scratched_section))
        self.match_count = len(self.winning_nums & self.scratched)
        self.copies = 1

    def __repr__(self) -> str:
        return "Card " + self.card_id

deck = list(map(Card, lines))

for c, card in enumerate(deck):
    start = c + 1
    end = min(start + card.match_count, len(deck))
    for i in range(start, end):
        deck[i].copies += card.copies

card_count = sum([c.copies for c in deck])
print(card_count)
