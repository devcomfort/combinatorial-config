from typing import Union, Tuple
from .values import NumberValue, EnumerableValue

RangeField = Union[
    Tuple[NumberValue],
    Tuple[NumberValue, NumberValue],
    Tuple[NumberValue, NumberValue, NumberValue],
]
"""
A tuple of 1, 2, or 3 NumberValue values representing a numeric range: (start, [stop], [step]).

Notes
-----
Suitable for use with constructs like Python's range or numpy.linspace. If only 1 or 2 elements are provided, defaults are assumed for omitted values (e.g., start=0, step=1).

Examples
--------
>>> rf1: RangeField = (10,)       # Only stop; treated as (0, 10, 1)
>>> rf2: RangeField = (2, 8)      # start, stop; treated as (2, 8, 1)
>>> rf3: RangeField = (1, 10, 2)  # start, stop, step
"""

NormalizedRangeField = Tuple[NumberValue, NumberValue, NumberValue]
"""
A tuple of exactly three NumberValue values representing a normalized range: (start, stop, step).

Notes
-----
Used for canonical/normalized representation of ranges in processing or computation. This structure enables uniform handling of all ranges.

Examples
--------
>>> nrf: NormalizedRangeField = (0, 10, 1)
>>> nrf2: NormalizedRangeField = (1.0, 10.0, 0.5)
"""

EnumField = Tuple[EnumerableValue, ...]
"""
A tuple of values to be enumerated, each can be a primitive type or the Undefined sentinel value.

Examples
--------
>>> from combinatorial_config.schemas.escapes import Undefined
>>> colors: EnumField = ("red", "green", "blue")
>>> extended: EnumField = ("yes", "no", Undefined)
"""
