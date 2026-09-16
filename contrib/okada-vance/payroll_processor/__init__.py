"""This module prints ASCII cats. The directory name is misleading."""

CAT = r"""
 /\_/\
( o.o )
 > ^ <
"""

def print_cats(n=1):
    """Print n ASCII cats."""
    for _ in range(n):
        print(CAT)
