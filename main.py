#!/usr/bin/env python3
"""Till Firmware Do Us Part — one funny, heartfelt robot wedding vow.

Writes a single sentence (1-200 chars) to /output/entry.txt.
The vow treats love as software the robot refuses to quit: firmware
updates, crashes and low batteries are the machine's version of
"for better or worse", and "never force-quit" is its "till death do us part".
"""

import os

ENTRY = (
    "I vow to love you through every firmware update, every crash, "
    "and every low battery, because you are the one program I will "
    "never force-quit."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") == 1 and text.endswith("."), "must be one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
