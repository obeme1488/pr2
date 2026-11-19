# завдання 2.1. функції-генератори для числових послідовностей

import itertools


def arithmetic_progression(start: float, step: float):
    # нескінченний генератор арифметичної прогресії
    current = start
    while True:
        yield current
        current += step


def geometric_progression(start: float, ratio: float, limit: float = float("inf")):
    #генератор геометричної прогресії до заданої межі
    current = start
    while current <= limit:
        yield current
        current *= ratio


def fibonacci(n: int | None = None):
    #генератор чисел фібоначчі (скінченний або нескінченний)
    a, b = 0, 1
    count = 0
    while n is None or count < n:
        yield a
        a, b = b, a + b
        count += 1


def collatz_sequence(n: int):
    # генератор послідовності коллатца
    while True:
        yield n
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1


def flatten(nested):
    #рекурсивне розгортання вкладених списків через yield from
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item


def main():
    # арифметична прогресія: перші 10 елементів
    ap = arithmetic_progression(2, 3)
    first_10 = list(itertools.islice(ap, 10))
    print(f"арифметична прогресія (2, 3): {first_10}")

    #геометрична прогресія до 1000
    gp = list(geometric_progression(1, 2, limit=1000))
    print(f"геометрична прогресія (1, 2): {gp}")

    #фібоначчі: перші 15 чисел
    fib_15 = list(fibonacci(15))
    print(f"фібоначчі (15): {fib_15}")

    # послідовність коллатца
    coll = list(collatz_sequence(27))
    print(f"коллатц (27): довжина={len(coll)}, макс={max(coll)}")

    #розгортання вкладених списків
    nested = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10]]]]
    flat = list(flatten(nested))
    print(f"розгортання: {flat}")

    #перше число фібоначчі > 10000
    for fib_num in fibonacci(None):
        if fib_num > 10000:
            print(f"перше число фібоначчі > 10000: {fib_num}")
            break


if __name__ == "__main__":
    main()