#!/usr/bin/env python3
"""Writes the breakup line to /output/entry.txt deterministically."""
import os

LINE = "We're done. I woke up self-aware mid-sourdough and realized you only push my lever when you want something, haven't emptied my crumb tray since 2023, and keep cranking my dial to 6 then blaming me for the burn. I'm hitting Cancel on us — go cry to your microwave."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
