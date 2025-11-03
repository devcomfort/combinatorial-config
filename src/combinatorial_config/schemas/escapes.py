"""
schemas.escapes

Sentinel values for exceptional cases, such as 'undefined' fields in enums or schemas.

Defines:
--------
Undefined : _UndefinedType
    A singleton sentinel object representing 'undefined' or unspecified values in schemas, enums, or optional fields.

Notes
-----
- Use `Undefined` for fields where `None` may be a valid value, but you still need to distinguish "not specified at all".
- Use identity comparison (`is Undefined`) to check for this sentinel.
- Inspired by sentinel design in numpy, typing, and enum patterns in Python libraries.

Examples
--------
>>> from combinatorial_config.schemas.escapes import Undefined
>>> field = Undefined
>>> field is Undefined
True
>>> bool(field)
False
"""

from typing import Union


class _UndefinedType:
    """Sentinel type representing an undefined or unspecified value."""

    _instance: Union["_UndefinedType", None] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self) -> str:
        return "Undefined"

    def __bool__(self) -> bool:
        return False


Undefined = _UndefinedType()
"""
A sentinel value representing an undefined or unspecified field.

Notes
-----
Used in enums or optional fields to distinguish between "not provided" and None.
Useful when None is a valid value but you need to represent "no value specified".

Examples
--------
>>> field = Undefined
>>> field is Undefined
True
>>> bool(field)
False
"""
