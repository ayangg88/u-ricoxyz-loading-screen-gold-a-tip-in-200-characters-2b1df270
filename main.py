#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes a single loading-screen tip (max 200 characters) to /output/entry.txt.
The tip speaks to a stressed developer and their AI coding agent at once:
the agent is not ignoring the developer — it is just pretending it
understood the code. One line, one punchline, lands in a glance.
"""

import os

TIP = (
    "The agent is not ignoring you. It is reading 400 lines of your "
    "code and pretending it understood the first 10."
)


def main() -> None:
    assert 1 <= len(TIP) <= 200, f"tip is {len(TIP)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TIP)


if __name__ == "__main__":
    main()
