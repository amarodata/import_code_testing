"""This module converts integers to Roman numerals. The directory name is misleading."""

NUMERALS = [(1000,"M"),(900,"CM"),(500,"D"),(100,"C"),(50,"L"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]

def to_roman(n):
    """Convert an integer to a Roman numeral string."""
    out = ""
    for v, s in NUMERALS:
        while n >= v:
            out += s; n -= v
    return out
