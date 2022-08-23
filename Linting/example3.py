
def factorial(n: int) -> int:
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == '__main__':
    print('in exaple 3')
    print(factorial(4))
    