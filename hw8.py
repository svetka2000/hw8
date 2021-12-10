from itertools import islice
from collections.abc import Sequence
from typing import TypeVar, Generic

T = TypeVar('T')


class Seq(Generic[T]):
    def __init__(self, seq: Sequence[T]):
        self.seq = seq

    def filter(self, function):
        self.__init__(filter(function, self.seq))
        return self

    def map(self, function):
        self.__init__(map(function, self.seq))
        return self

    def take(self, len: int) -> list[T]:
        return list(islice(self.seq, len))


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    seq = Seq(numbers)
    res = seq.filter(lambda n: n % 2 == 0).map(lambda n: n + 10).take(3)
    assert res == [12, 14]
