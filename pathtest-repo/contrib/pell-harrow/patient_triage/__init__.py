"""This module scales a banana bread recipe up or down. The directory name is misleading."""

BASE_BANANAS = 3

def scale(loaves):
    """Multiply the banana bread ingredients for N loaves."""
    return {"bananas": BASE_BANANAS*loaves, "flour_g": 190*loaves, "sugar_g": 150*loaves}
