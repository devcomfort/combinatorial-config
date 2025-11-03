"""
validators.fields

Validators and type guards for schema field objects (e.g., EnumField, RangeField).

Defines
-------
- is_range_field: Check if a value conforms to RangeField specification.
- is_enum_field: Check if a value conforms to EnumField specification.

Notes
-----
These helpers enable correct validation, type-checking, and runtime verification for schema fields.
They complement definitions in combinatorial_config.schemas.fields for robust schema handling.

Examples
--------
>>> from combinatorial_config.validators.fields import is_range_field, is_enum_field
>>> is_range_field((1, 10))
True
>>> is_enum_field(("on", "off"))
True
"""

from typing import Any, TypeGuard
from ..schemas.fields import RangeField, EnumField


def is_range_field(value: Any) -> TypeGuard[RangeField]:
    """
    Check if value is a tuple with 1, 2, or 3 numeric (int or float) elements, suitable for RangeField.

    Parameters
    ----------
    value : Any
        Value to check for RangeField type.

    Returns
    -------
    TypeGuard[RangeField]
        True if value is a tuple with 1-3 int or float entries, False otherwise.

    Examples
    --------
    >>> is_range_field((5,))
    True
    >>> is_range_field((1, 10, 2))
    True
    >>> is_range_field((1, 2, 3, 4))
    False
    >>> is_range_field([1, 2])
    False
    """
    if not isinstance(value, tuple):
        return False
    if len(value) not in {1, 2, 3}:
        return False
    return all(isinstance(v, (int, float)) for v in value)


def is_enum_field(value: Any) -> TypeGuard[EnumField]:
    """
    Check if value is a tuple with one or more enum-allowed elements (primitive or Undefined sentinel).

    Parameters
    ----------
    value : Any
        Value to check for EnumField type.

    Returns
    -------
    TypeGuard[EnumField]
        True if value is a tuple, length >= 1, all entries are primitive or Undefined sentinel.

    Examples
    --------
    >>> from combinatorial_config.schemas.escapes import Undefined
    >>> is_enum_field(("on", "off"))
    True
    >>> is_enum_field(("yes", Undefined))
    True
    >>> is_enum_field((1, 2, None))
    False
    >>> is_enum_field((True,))
    True
    >>> is_enum_field([])
    False
    """
    if not isinstance(value, tuple):
        return False
    if len(value) == 0:
        return False
    return all(
        isinstance(v, (int, float, str, bool)) or type(v).__name__ == "_UndefinedType"
        for v in value
    )
