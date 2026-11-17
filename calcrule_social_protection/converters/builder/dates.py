def date_or_none(value):
    """Serialises a date for the bill and benefit data; an open-ended validity stays None."""
    return None if value is None else f"{value}"
