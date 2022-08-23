from concurrent.futures.process import _process_worker


def pow_of_two(n: int) -> dict[int, int]:
    return {i: 2 ** i for i in range(n)}

if __name__ == "__main__":
    d = pow_of_two(5)
    print(d[3])
    