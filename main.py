#!/usr/bin/env python3
"""Write one missed-deadline excuse to /output/entry.txt (pure stdlib)."""
import os

EXCUSE = (
    "I finished on time, but context compaction summarized the deliverable, "
    "the deadline, and my memory of agreeing to either."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 200, "excuse must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
