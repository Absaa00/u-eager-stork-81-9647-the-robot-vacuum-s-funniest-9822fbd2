#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Writes one line (at most 120 characters): the excuse a robot vacuum
gives for missing a spot. Deterministic, no network, no randomness.

The joke is told in the vacuum's own voice: its suction saw the dust
bunny, filed for workers' comp, and went on strike — a machine making
peace with its failure, in its own world of suction and dust.
"""
import os

LINE = "I didn't miss that spot - my suction saw the dust bunny, filed for workers' comp, and went on strike."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
