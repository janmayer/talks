---
marp: true
theme: uncover
#class: invert
style: |
  h1 {
    font-size: 170%;
  }
---

# Typing in Python 3.12

Jan Mayer, 20.10.23

- New Type Parameter Syntax
- Type Annotations for kwargs
- @override
- Bonus: itertools.batched

---

## Why care about typing?

- Developer Experience & Productivity
    - IDE Autocomplete (IntelliSense) <!-- Enables faster code writing and reduced lookup time. -->
    - Real-Time IDE Feedback (red squiggly lines) <!-- Immediate feedback on potential issues without executing the code. -->
    <br><br>
- Improved Readability / Self-Documenting Code <!-- Type hints make code intentions clear, aiding future readers and maintainers. -->
- Early Error Detection and Debugging
    - Fearless Refactoring
    - Static Analysis in Pipelines (mypy / pyright)
- Code Quality Bragging Rights

---

## New Type Parameter Syntax

---

```python
def batched(items, size):
    """
    Split a list of items into batches of a specified size.

    :param items: List of items to be split.
    :param size: Size of each batch.
    :return: List of batches.

    >>> batched([1, 2, 3, 4, 5], 2)
    [[1, 2], [3, 4], [5]]
    """
    return [items[i:i + size] for i in range(0, len(items), size)]
```

<!--
    What is the correct way to annotate a generic function?
-->

---

```python
def batched(items, size):
```

```text
error: Type of parameter "items" is unknown (reportUnknownParameterType)
error: Type annotation is missing for parameter "items" (reportMissingParameterType)
error: Type of parameter "size" is unknown (reportUnknownParameterType)
error: Type annotation is missing for parameter "size" (reportMissingParameterType)
error: Argument type is unknown
Argument corresponds to parameter "__obj" in function "len" (reportUnknownArgumentType)
error: Argument type is unknown
Argument corresponds to parameter "__step" in function "__new__" (reportUnknownArgumentType)
error: Return type, "list[Unknown]", is partially unknown (reportUnknownVariableType)
error: Return type, "list[Unknown]", is partially unknown (reportUnknownParameterType)
8 errors, 0 warnings, 0 informations
```

<!--
Fully untyped:
Note: "partially unknown" is actually not that bad
-->

---

```python
def batched(items: list[Any], size: int) -> list[list[Any]]:
```

```text
0 errors, 0 warnings, 0 informations
```

---

```python
def batched(items: list[Any], size: int) -> list[list[Any]]:
```

🚫 Worse than no type hints!

---

```python
T = TypeVar('T')

def batched(items: list[T], size: int) -> list[list[T]]:
```

<!--
Super annoying. No longer self-contained. TypeVar floating around.
-->

---

```python
def batched[T](items: list[T], size: int) -> list[list[T]]:
```

---

```python
@dataclass
class Car[T]:
    brand: str
    year: int
    engine: T
```
```python
type Point = tuple[float, float]
```
```python
type Point[T] = tuple[T, T]
```
```python
type IntFunc[**P] = Callable[P, int]  # ParamSpec
type LabeledTuple[*Ts] = tuple[str, *Ts]  # TypeVarTuple
type HashableSequence[T: Hashable] = Sequence[T]  # TypeVar with bound
type IntOrStrSequence[T: (int, str)] = Sequence[T]  # TypeVar with constraints
```

<!--
The new syntax allows declaring TypeVarTuple and ParamSpec parameters, as well as TypeVar parameters with bounds or constraints:
-->

---

## Type Annotations for kwargs

---

```python
def myfun(**kwargs: int):
```

---

```python
def myfun(**kwargs: int):  # kwargs is dict[str, int]
```

---

```python
def myfun(**kwargs: int | str):  # kwargs is dict[str, int | str]
```

---

```python
from typing import TypedDict


class Car(TypedDict):
    brand: str
    year: int


def myfun(**kwargs: Car):  # kwargs is dict[str, Car]
```

---

```python
from typing import TypedDict, Unpack


class Car(TypedDict):
    brand: str
    year: int


def myfun(**kwargs: Unpack[Car]):  # kwargs is Car (which is still a dict)
```

<!--
Really the only usecase for TypedDict
-->
---

```python
class Car(TypedDict):
   brand: str
   year: NotRequired[int]

car1: Car = {"brand": "seat", "year": 2018}  # OK
car2: Car = {"brand": "skoda"}  # OK (year is not required)
car3: Car = {"year": 2022}  # ERROR (missing required field brand)

class Car(TypedDict, total=False):  # equivalent
   brand: Required[str]
   year: int
```

---

## @override

---

```python
class Vehicle(ABC): # Abstract base class (~Interface)
    @abstractmethod
    def refill(self):
        pass

class ElectricVehicle(Vehicle):
    @override
    def refill(self):
        ... # Charging logic

class InternalCombustionVehicle(Vehicle):
    @override
    def refill(self):
        ... # Refueling logic
```

---

- Type Parameter Syntax -> **10/10**
- Type Annotations for kwargs -> **06/10**
- @override -> **03/10**
- Itertools.batched **10/10**
