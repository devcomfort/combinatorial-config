from .schemas import NormalizedRangeField, RangeField


def normalize_range_field(value: RangeField) -> NormalizedRangeField:
    """
    Normalize various forms of RangeField into a 3-element (start, stop, step) tuple.

    Parameters
    ----------
    value : RangeField
        A tuple specifying a range, one of:
        - (stop,)
        - (start, stop)
        - (start, stop, step)
        Each element can be int or float.

    Returns
    -------
    NormalizedRangeField
        A 3-element tuple (start, stop, step), all values are int or float.

    Raises
    ------
    ValueError
        If value is not a tuple, not length 1-3, or its elements are not all int or float.

    Examples
    --------
    >>> normalize_range_field((5,))
    (0, 5, 1)
    >>> normalize_range_field((2, 8))
    (2, 8, 1)
    >>> normalize_range_field((1, 10, 2))
    (1, 10, 2)
    >>> normalize_range_field((0.0, 1.0, 0.1))
    (0.0, 1.0, 0.1)
    >>> normalize_range_field(("a",))
    Traceback (most recent call last):
        ...
    ValueError: Invalid range field: ('a',)
    """
    if not isinstance(value, tuple) or not all(
        isinstance(v, (int, float)) for v in value
    ):
        raise ValueError(f"Invalid range field: {value}")

    if len(value) == 1:
        return (0, value[0], 1)
    elif len(value) == 2:
        return (value[0], value[1], 1)
    elif len(value) == 3:
        return (value[0], value[1], value[2])
    else:
        raise ValueError(f"Invalid range field: {value}")
