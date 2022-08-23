from re import X
from typing import Generator


def powers_of_two(n: int) -> list[int]:
    return [2 ** i for i in range(n)]


def powers_of_two_generator(n: int) -> Generator[int, None, None]:
    return (2 ** x for x in range(n))


def powers_of_two_generator_version2(n: int) -> Generator[int, None, None]:
    x = 1
    for _ in range(n):
        yield x
        x += 2

def my_generator() -> Generator[int, None, None]:
    yield 4
    yield 8
    yield 15


if __name__ == "__main__":
    # print(powers_of_two(10))
    # g = powers_of_two_generator(1_000_000)
    # for _ in range(10):
    #     print(next(g))
    g = my_generator()
    print(next(g))
    print(next(g))