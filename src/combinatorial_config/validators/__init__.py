"""
validators

Validation utilities and type guards for combinatorial configuration schemas.

This subpackage provides functions to check and enforce correctness for fields, values, and sentinel types
used throughout the schema definitions in `combinatorial_config.schemas`.

Submodules
----------
fields
    Validators and type guards for schema field objects (e.g., EnumField, RangeField).
values
    Validators and type guards for scalar or enumerated field values.
escapes
    Validators for special sentinel types such as Undefined.

Examples
--------
>>> from combinatorial_config.validators import fields, values, escapes
>>> fields.is_range_field((0, 1, 2))
True
>>> values.is_enumerable_value("foo")
True
"""

from .values import is_number_value, is_primitive_value, is_enumerable_value
from .fields import is_range_field, is_enum_field
from .escapes import is_undefined

__all__ = [
    "is_number_value",
    "is_primitive_value",
    "is_enumerable_value",
    "is_range_field",
    "is_enum_field",
    "is_undefined",
]
