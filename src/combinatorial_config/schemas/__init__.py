"""
schemas

Canonical type building blocks, field representations, and explicit sentinels
for combinatorial configuration schemas.

This package unifies all types, value unions, range and enum field specs, and sentinel values
for strict schema construction, validation, and runtime editing of configuration domains.

Exports
-------
NumberValue : int | float
    Numeric types for scalar/range fields (e.g. parameter bounds, step sizes).
PrimitiveValue : int | float | str | bool
    Literal types allowed for direct user input or as enum/literal values.
EnumerableValue : PrimitiveValue | _UndefinedType
    Union for values that enumerate primitives and the explicit "Undefined" sentinel for
    optional/unspecified states. Used for enums, option sets, etc.
RangeField : tuple
    Tuple of 1-3 int/float (start, stop[, step]), with normalization utilities available.
NormalizedRangeField : tuple
    Strict 3-tuple (start, stop, step) normalizing all RangeField forms.
EnumField : tuple
    One or more EnumerableValue instances specifying admissible field options.
Undefined : _UndefinedType instance
    Singleton sentinel for fields explicitly 'not set' or 'unspecified'. Use for runtime logic and assignments,
    and compare with `is` (identity check only).
_UndefinedType : type
    Sentinel class (never instantiate yourself). For use only in type annotations.

Design
------
- Types and sentinels are organized in submodules (values, fields, escapes) for clarity and strict import hygiene.
- Use Undefined for value assignment/check; use _UndefinedType in `Union` or function signatures for static type checking only.
- Explicit separation of runtime value and type avoids silent None-misuse and increases type safety for users and library code.
- RangeField/EnumField specs are always tuples. Accepts both ints and floats, and is validated/normalized before use in algorithms.

Submodules
----------
values
    Fundamental and derived value types; unions for primitive/configured values.
fields
    Field representations and constraints for ranges, enums, and normalized forms.
escapes
    Sentinel type and singleton value for undefined/unspecified field values.

Examples
--------
>>> from combinatorial_config.schemas import EnumField, Undefined, RangeField
>>> bar: EnumField = ("on", "off", Undefined)
>>> assert bar[2] is Undefined
>>> rf: RangeField = (9, 10)
>>> # All types strictly typed, normalized and validated for downstream logic
"""

from .values import NumberValue, PrimitiveValue, EnumerableValue
from .fields import RangeField, EnumField, NormalizedRangeField
from .escapes import Undefined, _UndefinedType

__all__ = [
    "NumberValue",
    "PrimitiveValue",
    "EnumerableValue",
    "RangeField",
    "NormalizedRangeField",
    "EnumField",
    "Undefined",
    "_UndefinedType",
]
