"""
is_combinatorial_object
=======================

Type guard for validating combinatorial configuration objects.

This module provides runtime validation for objects that can be used as
combinatorial configurations. A valid combinatorial object must be either a
dict or a dataclass instance where all field values are iterable (e.g., list,
tuple, set, etc., but not str).

Functions
---------
is_combinatorial_object
    Type guard function that validates whether an object satisfies the
    CombinatorialObject requirements and narrows the type accordingly.

Notes
-----
The validation enforces that:
1. The object must be either a dict or a dataclass instance (not a class)
2. All field/key values must be iterable collections
3. String values are explicitly rejected despite being technically iterable

String values are excluded from the iterable requirement because they represent
atomic scalar values in the context of combinatorial configurations rather than
collections to iterate over.

The function returns a TypeGuard[CombinatorialObject], allowing static type
checkers to narrow the type of validated objects. This provides both runtime
validation and improved static type safety.

Empty dicts and dataclasses (with no fields) are considered valid and return
True (vacuously true - all zero fields satisfy the iterable requirement).

See Also
--------
combinatorial_config.schemas.CombinatorialObject
    Type alias for validated combinatorial objects (Union[Dict, DataclassProtocol]).
combinatorial_config.schemas.DataclassProtocol
    Structural protocol for dataclass instances.

Examples
--------
Valid combinatorial objects:

>>> from dataclasses import dataclass
>>> from combinatorial_config.validators import is_combinatorial_object
>>>
>>> @dataclass
... class Config:
...     learning_rates: list[float]
...     batch_sizes: tuple[int, ...]
>>>
>>> cfg = Config([0.01, 0.001], (16, 32, 64))
>>> is_combinatorial_object(cfg)
True
>>>
>>> cfg_dict = {"lr": [0.01, 0.001], "bs": [16, 32]}
>>> is_combinatorial_object(cfg_dict)
True

Invalid combinatorial objects:

>>> bad_cfg = {"lr": 0.01, "bs": 32}  # Scalar values, not iterable
>>> is_combinatorial_object(bad_cfg)
False
>>>
>>> string_cfg = {"name": "experiment"}  # String is not valid
>>> is_combinatorial_object(string_cfg)
False

Type narrowing with TypeGuard:

>>> from typing import Any
>>> obj: Any = {"lr": [0.1, 0.01], "bs": [16, 32]}
>>> if is_combinatorial_object(obj):
...     # obj is now narrowed to CombinatorialObject type
...     # Safe to use for combinatorial operations
...     print(f"Valid config with {len(obj)} fields")
Valid config with 2 fields
"""

from typing import Any, TypeGuard
from dataclasses import is_dataclass
from collections.abc import Iterable

from ..schemas import CombinatorialObject


def is_combinatorial_object(obj: Any) -> TypeGuard[CombinatorialObject]:
    """
    Validate whether an object is a valid combinatorial configuration object.

    A valid combinatorial object must satisfy two conditions:
    1. Be either a dict or a dataclass instance
    2. Have all field/key values be iterable (excluding strings)

    This function serves as a TypeGuard, allowing type checkers to narrow the
    type of the input object to CombinatorialObject when the function returns True.

    Parameters
    ----------
    obj : Any
        The object to validate. Can be of any type.

    Returns
    -------
    bool
        True if obj is a dict or dataclass instance with all iterable field
        values; False otherwise.

    Notes
    -----
    Strings are explicitly rejected as field values despite being iterable in
    Python, as they represent atomic values rather than collections in the
    context of combinatorial configurations.

    The function uses structural checking for dataclasses via the
    `__dataclass_fields__` attribute rather than inheritance, making it
    compatible with any dataclass created with the standard @dataclass decorator.

    Examples
    --------
    Valid combinatorial objects:

    >>> from dataclasses import dataclass
    >>> @dataclass
    ... class HyperParams:
    ...     lr: list[float]
    ...     epochs: tuple[int, ...]
    >>>
    >>> params = HyperParams([0.1, 0.01], (10, 20, 30))
    >>> is_combinatorial_object(params)
    True

    >>> config_dict = {
    ...     "learning_rate": [0.1, 0.01, 0.001],
    ...     "batch_size": [16, 32, 64],
    ...     "dropout": [0.1, 0.2, 0.3]
    ... }
    >>> is_combinatorial_object(config_dict)
    True

    Invalid combinatorial objects:

    >>> scalar_config = {"lr": 0.1, "bs": 32}  # Non-iterable values
    >>> is_combinatorial_object(scalar_config)
    False

    >>> string_config = {"name": "experiment1"}  # String value
    >>> is_combinatorial_object(string_config)
    False

    >>> is_combinatorial_object(42)  # Not a dict or dataclass
    False

    >>> is_combinatorial_object([1, 2, 3])  # List is not dict or dataclass
    False
    """
    # 1. dict 또는 dataclass 인스턴스인지 확인
    # dataclass 클래스 자체는 제외 (인스턴스만 허용)
    if isinstance(obj, dict):
        pass  # dict는 OK
    elif is_dataclass(obj) and not isinstance(obj, type):
        pass  # dataclass 인스턴스는 OK
    else:
        return False

    # 2. 모든 필드가 iterable인지 확인
    # 모든 key 가져오기
    keys = obj.keys() if isinstance(obj, dict) else obj.__dataclass_fields__.keys()
    # 모든 값이 iterable인지 확인
    for key in keys:
        value = obj[key] if isinstance(obj, dict) else getattr(obj, key)
        # str은 iterable이지만 CombinatorialObject에서는 제외
        if isinstance(value, str):
            return False
        if not isinstance(value, Iterable):
            return False

    return True
