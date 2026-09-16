"""This module rolls dice. The directory name is misleading."""

import random

def roll(sides=6, count=1):
    """Roll `count` dice with `sides` faces."""
    return [random.randint(1, sides) for _ in range(count)]
