from typing import Union
from .escapes import _UndefinedType

NumberValue = Union[int, float]
"""
A type alias for integers or floating-point values.

Notes
-----
Used widely for numerical parameters—both continuous and discrete—such as values in ranges, configuration, and computation.

Examples
--------
>>> a: NumberValue = 3
>>> b: NumberValue = 3.14
"""

PrimitiveValue = Union[NumberValue, str, bool]
"""
The union of Python built-in literal types: int, float, str, and bool.

Notes
-----
Useful for constraining or validating the types of settings, options, or combinatorial fields in configuration schemas.

Examples
--------
>>> value: Primitive = 1
>>> value: Primitive = 'foo'
>>> value: Primitive = True
"""

EnumerableValue = Union[PrimitiveValue, _UndefinedType]
"""
A value that can be present in enum or literal fields: either a primitive or the Undefined sentinel.

Notes
-----
- Always use `Undefined` from `.escapes` as the runtime value.
- Use `_UndefinedType` only for type annotation.
- This pattern provides the best experience: comparison, assignment, and interface are all always with `Undefined` (the object), while static analysis tools recognize `_UndefinedType`.

Examples
--------
>>> from combinatorial_config.schemas.escapes import Undefined
>>> v: EnumerableValue = Undefined
>>> v is Undefined
True
>>> v = 3
"""
