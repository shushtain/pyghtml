"""Utility functions"""

from collections.abc import Sequence
from typing import Any

from .tags import _Tag, _Container

# Sentinel object for unset values, since None is a valid value
UNSET = object()


def contains(item: Any, container: Sequence, deep: bool = False) -> bool:
    """Returns `True` if the item is in the container. Otherwise returns `False`. Use `deep=True` to search recursively"""
    if isinstance(container, Sequence) and not isinstance(container, (str, bytes)):
        for element in container:
            if item == element:
                return True
            if deep and contains(item, element, deep):
                return True
    return False


def find_by_tag(container: _Container, tag: str, deep: bool = False) -> list:
    """Returns a list of children with the specified tag. Otherwise returns an empty list. Use `deep=True` to search recursively"""
    results = []
    if isinstance(container, _Container):
        for element in container:
            if isinstance(element, _Tag) and element.tag() == tag:
                results.append(element)
            if deep:
                results.extend(find_by_tag(element, tag, deep))
    return results


def find_by_attr(
    container: _Container, attr: str, value: Any = UNSET, deep: bool = False
) -> list:
    """Returns a list of children that support the specified attribute (optionally matching a value). Otherwise returns an empty list. Use `deep=True` to search recursively"""
    results = []
    if isinstance(container, _Container):
        for element in container:
            if isinstance(element, _Tag) and hasattr(element, attr):
                attr_value = getattr(element, attr)
                if value is UNSET or attr_value == value:
                    results.append(element)
            if deep:
                results.extend(find_by_attr(element, attr, value, deep))
    return results


def sub(
    container: _Container, old: Any, new: Any, deep: bool = False, count: int = -1
) -> _Container:
    """Substitutes children within a container. Returns the container. Use `deep=True` to replace recursively. Use `count` to limit the number of replacements"""
    if count < -1 or not isinstance(count, int):
        raise ValueError("Count must be -1 (replace all) or a non-negative integer")
    if isinstance(container, _Container):
        for i, element in enumerate(container):
            if element == old:
                if count != 0:
                    container[i] = new
                    if count > 0:
                        count -= 1
                    continue
            if deep and count != 0:
                container[i] = sub(element, old, new, deep, count)
    return container
