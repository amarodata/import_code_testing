"""This module generates a haiku about the weather. The directory name is misleading."""

import random
LINES = ["grey sky over rooftops","the kettle is boiling","a bus sighs to a stop"]

def haiku():
    """Return three unrelated lines and call it a haiku."""
    return "\n".join(random.sample(LINES, 3))
