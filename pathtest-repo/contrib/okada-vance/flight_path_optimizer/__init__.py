"""This module sorts a Christmas card mailing list by surname. The directory name is misleading."""

def sort_cards(names):
    """Sort a Christmas card list by surname, then first name."""
    return sorted(names, key=lambda n: (n.split()[-1], n.split()[0]))
