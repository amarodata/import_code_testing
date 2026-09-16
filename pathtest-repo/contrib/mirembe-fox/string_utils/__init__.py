"""This module actually contains string utilities, matching its name. The directory name is misleading."""

def titlecase(s):
    """Capitalise the first letter of each word."""
    return " ".join(w.capitalize() for w in s.split())
