from typing import Any, TypeGuard
from .schemas import Number, Primitive, RangeField, EnumField, Literal


def is_number(value: Any) -> TypeGuard[Number]:
    """
    Check if the value is an int or float (Number type).

    Parameters
    ----------
    value : Any
        Value to check for number type.

    Returns
    -------
    TypeGuard[Number]
        True if value is int or float, False otherwise.

    Examples
    --------
    >>> is_number(3)
    True
    >>> is_number(4.5)
    True
    >>> is_number("x")
    False
    """
    return isinstance(value, (int, float))


def is_primitive(value: Any) -> TypeGuard[Primitive]:
    """
    Check if value is a Primitive (int, float, str, or bool).

    Parameters
    ----------
    value : Any
        Value to check for primitive type.

    Returns
    -------
    TypeGuard[Primitive]
        True if value is int, float, str, or bool; otherwise False.

    Examples
    --------
    >>> is_primitive(0)
    True
    >>> is_primitive('foo')
    True
    >>> is_primitive(False)
    True
    >>> is_primitive([1, 2])
    False
    """
    return isinstance(value, (int, float, str, bool))


def is_range_field(value: Any) -> TypeGuard[RangeField]:
    """
    Check if value is a tuple of length 1, 2, or 3 (RangeField type).

    Parameters
    ----------
    value : Any
        Value to check for RangeField type.

    Returns
    -------
    TypeGuard[RangeField]
        True if value is a tuple with 1, 2, or 3 items, False otherwise.

    Examples
    --------
    >>> is_range_field((1,))
    True
    >>> is_range_field((3, 5))
    True
    >>> is_range_field((1, 2, 3))
    True
    >>> is_range_field((1, 2, 3, 4))
    False
    >>> is_range_field([1, 2])
    False
    """
    return isinstance(value, tuple) and (
        len(value) == 1 or len(value) == 2 or len(value) == 3
    )


def is_enum_field(value: Any) -> TypeGuard[EnumField]:
    """
    Check if value is an EnumField, i.e. a tuple of one or more primitives.

    Parameters
    ----------
    value : Any
        Value to check for EnumField type.

    Returns
    -------
    TypeGuard[EnumField]
        True if value is a tuple, non-empty, with all items Primitive.

    Examples
    --------
    >>> is_enum_field((1, 2, 3))
    True
    >>> is_enum_field(("apple", "banana"))
    True
    >>> is_enum_field(())
    False
    >>> is_enum_field([1, 2])
    False
    """
    return (
        isinstance(value, tuple)
        and all(isinstance(item, Primitive) for item in value)
        and len(value) > 0
    )


def is_literal(value: Any) -> TypeGuard[Literal]:
    """
    Check if value is a Literal (int, float, str, or bool).

    Parameters
    ----------
    value : Any
        Value to check for Literal type.

    Returns
    -------
    TypeGuard[Literal]
        True if value is int, float, str, or bool; otherwise False.

    Examples
    --------
    >>> is_literal(1)
    True
    >>> is_literal('bar')
    True
    >>> is_literal(None)
    False
    """
    return isinstance(value, Primitive)
