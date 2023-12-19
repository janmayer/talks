# pyright: strict
from typing import TypedDict, Unpack

class Car(TypedDict):
    brand: str
    year: int


def myfun(**kwargs: Unpack[Car]):  # kwargs is Car (which is still a dict)
    print(kwargs['brand'])


myfun()
