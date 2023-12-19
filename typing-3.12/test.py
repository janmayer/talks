# pyright: strict
from typing import Any, TypeVar

T = TypeVar('T')

#def batched(items, size):
# def batched(items: list[Any], size: int) -> list[list[Any]]:
# def batched(items: list[T], size: int) -> list[list[T]]:
def batched_template[T](items: list[T], size: int) -> list[list[T]]:
    return [items[i:i + size] for i in range(0, len(items), size)]
