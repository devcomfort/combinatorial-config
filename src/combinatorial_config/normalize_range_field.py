"""
normalize_range_field

Utilities for validating and normalizing range fields in combinatorial configuration schemas.

Exports
-------
normalize_range_field(value: RangeField) -> NormalizedRangeField
    Normalize various forms of RangeField to a standard 3-tuple representation.

Notes
-----
- A RangeField is a tuple of length 1, 2, or 3 containing only int or float values.
- This utility enforces type and structural constraints and normalizes to (start, stop, step) format.
- Uses is_range_field from the validators subpackage for robust validation.
- Raises ValueError on invalid input.

Examples
--------
>>> from combinatorial_config.normalize_range_field import normalize_range_field
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

from .schemas import NormalizedRangeField, RangeField
from .validators import is_range_field


def normalize_range_field(value: RangeField) -> NormalizedRangeField:
    """
    Normalize various forms of RangeField into a 3-element (start, stop, step) tuple.

    Parameters
    ----------
    value : RangeField
        A tuple specifying a valid range, one of:
        - (stop,)
        - (start, stop)
        - (start, stop, step)
        Each element must be int or float.

    Returns
    -------
    NormalizedRangeField
        A 3-element tuple (start, stop, step); all elements are int or float.

    Raises
    ------
    ValueError
        If value is not a tuple, not of length 1-3, or its elements are not int or float.

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
    if not is_range_field(value):
        raise ValueError(f"Invalid range field: {value}")

    if len(value) == 1:
        return (0, value[0], 1)
    elif len(value) == 2:
        return (value[0], value[1], 1)
    elif len(value) == 3:
        return (value[0], value[1], value[2])
    else:
        raise ValueError(f"Invalid range field: {value}")
