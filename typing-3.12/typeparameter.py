# pyright: strict
from dataclasses import dataclass
from typing import Any, Literal, TypeVar
import itertools


@dataclass
class Car():
    brand: Literal["audi", "seat", "skoda", "vw"]
    year: int


def batched_untyped(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]


def batched_any(items: list[Any], size: int) -> list[list[Any]]:
    return [items[i:i + size] for i in range(0, len(items), size)]


U = TypeVar('U')

def batched_typevar(items: list[U], size: int) -> list[list[U]]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def batched_template[T](items: list[T], size: int) -> list[list[T]]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def do_something():
    cars = [Car(brand="audi", year=2000), Car(brand="seat", year=2001), Car(brand="skoda", year=2002), Car(brand="vw", year=2003)]
    #batched = batched_untyped(cars, 2)
    #batched = batched_any(cars, 2)
    #batched = batched_typevar(cars, 2)
    #batched = batched_template(cars, 2)
    batched = list(itertools.batched(cars, 2))
    print(batched[0][0].year)


do_something()
