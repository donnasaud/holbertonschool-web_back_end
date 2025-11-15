#!/usr/bin/env python3
"""Module containing the safely_get_value function."""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """safely_get_value function"""
    if key in dct:
        return dct[key]
    else:
        return default
