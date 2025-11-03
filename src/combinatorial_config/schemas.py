from typing import Tuple

Number = int | float
"""
A type alias for integers or floating-point values.

Notes
-----
Used widely for numerical parameters—both continuous and discrete—such as values in ranges, configuration, and computation.

Examples
--------
>>> a: Number = 3
>>> b: Number = 3.14
"""

Primitive = Number | str | bool
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

RangeField = Tuple[Number] | Tuple[Number, Number] | Tuple[Number, Number, Number]
"""
A tuple of 1, 2, or 3 Number values representing a numeric range: (start, [stop], [step]).

Notes
-----
Suitable for use with constructs like Python's range or numpy.linspace. If only 1 or 2 elements are provided, defaults are assumed for omitted values (e.g., start=0, step=1).

Examples
--------
>>> rf1: RangeField = (10,)       # Only stop; treated as (0, 10, 1)
>>> rf2: RangeField = (2, 8)      # start, stop; treated as (2, 8, 1)
>>> rf3: RangeField = (1, 10, 2)  # start, stop, step
"""

NormalizedRangeField = Tuple[Number, Number, Number]
"""
A tuple of exactly three Number values representing a normalized range: (start, stop, step).

Notes
-----
Used for canonical/normalized representation of ranges in processing or computation. This structure enables uniform handling of all ranges.

Examples
--------
>>> nrf: NormalizedRangeField = (0, 10, 1)
>>> nrf2: NormalizedRangeField = (1.0, 10.0, 0.5)
"""

EnumField = Tuple[Primitive, ...]
"""
A tuple of one or more Primitive values representing an enumerated set of valid options for a field.

Notes
-----
Useful for constraining setting values to a fixed list of options, such as discrete choices or categorical states.

Examples
--------
>>> colors: EnumField = ('red', 'green', 'blue')
>>> bools: EnumField = (True, False)
"""

Literal = Primitive
"""
A field type that accepts only a single value of int, float, str, or bool.

Notes
-----
Suitable for input fields restricted to one literal value, or for expressing required constants.

Examples
--------
>>> lit: Literal = 10
>>> lit: Literal = "on"
>>> lit: Literal = False
"""
