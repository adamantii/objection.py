"""Utility functions used across other files."""

from typing import Any, Iterable, Optional


def _reprFunc(obj, attributes: Iterable) -> str:
    result = '<'
    result += type(obj).__name__
    for key in attributes:
        result += ' ' + key + '=' + repr(getattr(obj, key))
    result += '>'
    return result


def _maxIndex(list: list) -> int:
    return list.index(max(list))

def _tupleMapGet(list: list[tuple[Any, Any]], firstValue):
    for tuple in list:
        if tuple[0] == firstValue:
            return tuple[1]
    raise KeyError(repr(firstValue) + ' is not in tuple map')
