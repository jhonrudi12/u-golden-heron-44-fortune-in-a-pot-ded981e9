#!/usr/bin/env python3
"""Fortune in a Pot — write one kind, funny fortune for a houseplant.

Deterministic, no network. Writes the fortune to /output/entry.txt
and prints it.
"""

import os

ENTRY = "This week, a sunbeam will find your tallest leaf, and you will spend all afternoon leaning into it like applause."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
