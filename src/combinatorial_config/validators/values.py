"""
validators.values

Validators and type guards for value objects used in schema fields.

Defines
-------
- is_number_value: Type guard for integers or floats.
- is_primitive_value: Type guard for allowed primitives (int, float, str, bool).
- is_enumerable_value: Type guard for primitives or Undefined sentinel values.

Examples
--------
>>> from combinatorial_config.validators.values import is_enumerable_value
>>> from combinatorial_config.schemas.escapes import Undefined
>>> is_enumerable_value(Undefined)
True
>>> is_enumerable_value(3.5)
True
>>> is_primitive_value("bar")
True
>>> is_number_value(4)
True
"""

from typing import Any, TypeGuard
from ..schemas.values import NumberValue, PrimitiveValue, EnumerableValue
from ..schemas.escapes import Undefined


def is_number_value(value: Any) -> TypeGuard[NumberValue]:
    """
    Check if value is an int or float (NumberValue).

    Parameters
    ----------
    value : Any
        Value to check for NumberValue type.

    Returns
    -------
    TypeGuard[NumberValue]
        True if value is int or float, False otherwise.

    Examples
    --------
    >>> is_number_value(1)
    True
    >>> is_number_value(1.234)
    True
    >>> is_number_value("1")
    False
    """
    return isinstance(value, (int, float))


def is_primitive_value(value: Any) -> TypeGuard[PrimitiveValue]:
    """
    Check if value is int, float, str, or bool (PrimitiveValue).

    Parameters
    ----------
    value : Any
        Value to check for PrimitiveValue type.

    Returns
    -------
    TypeGuard[PrimitiveValue]
        True if value is int, float, str, or bool; otherwise False.

    Examples
    --------
    >>> is_primitive_value(0)
    True
    >>> is_primitive_value("foo")
    True
    >>> is_primitive_value(False)
    True
    >>> is_primitive_value([1, 2])
    False
    """
    return isinstance(value, (int, float, str, bool))


def is_enumerable_value(value: Any) -> TypeGuard[EnumerableValue]:
    """
    Check if value is a PrimitiveValue or the Undefined sentinel (EnumerableValue).

    Parameters
    ----------
    value : Any
        Value to check for EnumerableValue type.

    Returns
    -------
    TypeGuard[EnumerableValue]
        True if value is a valid primitive or is Undefined sentinel.

    Examples
    --------
    >>> from combinatorial_config.schemas.escapes import Undefined
    >>> is_enumerable_value(Undefined)
    True
    >>> is_enumerable_value(1)
    True
    >>> is_enumerable_value("foo")
    True
    >>> is_enumerable_value([])
    False
    """
    return is_primitive_value(value) or value is Undefined
