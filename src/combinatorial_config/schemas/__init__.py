"""
schemas

Core type definitions and sentinel values for composable configuration schemas.

This subpackage aggregates and re-exports canonical schema field types, value types, and sentinel instances for use throughout the package.

Exports
-------
NumberValue : int | float
    Acceptable numeric types for schema fields (integers or floats).
PrimitiveValue : int | float | str | bool
    Keys or settings allowing Python-native scalar types.
EnumerableValue : PrimitiveValue | _UndefinedType
    Values usable in enumerated settings, including primitives and the Undefined sentinel.
RangeField : tuple
    Range specifications as 1-3 element tuples of numbers.
EnumField : tuple
    Allowed value set for a categorical field (tuple of EnumerableValue).
Undefined : _UndefinedType instance
    Sentinel for explicit 'undefined' field (distinct from None).

Notes
-----
Use these canonical types for all combinatorial schema definitions, validation, and introspection throughout the library and user code.

Examples
--------
>>> from combinatorial_config.schemas import EnumField, Undefined
>>> options: EnumField = ("x", "y", Undefined)
"""

from .values import NumberValue, PrimitiveValue, EnumerableValue
from .fields import RangeField, EnumField
from .escapes import Undefined

__all__ = [
    "NumberValue",
    "PrimitiveValue",
    "EnumerableValue",
    "RangeField",
    "EnumField",
    "Undefined",
]
