from typing import Iterator


class Range:
    def __init__(self, stop: int):
        self.start = 0
        self.stop = stop

    def __contains__(self, item):
        return isinstance(item, int) and 0 <= item < self.stop

    def __iter__(self) -> Iterator[int]:
        curr = self.start
        while curr < self.stop:
            yield curr
            curr += 1


print(42 in Range(100000000000000000000000000))

for n in Range(5):
    print(n)
