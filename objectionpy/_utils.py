from typing import Iterable, Optional


def _reprFunc(obj, attributes: Iterable) -> str:
    result = '<'
    result += type(obj).__name__
    for key in attributes:
        result += ' ' + key + '=' + repr(getattr(obj, key))
    result += '>'
    return result


def _maxIndex(lst: list) -> int:
    return lst.index(max(lst))
