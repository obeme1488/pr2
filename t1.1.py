# завдання 1.1. реалізація власного ітератора CyclicRange

class CyclicRange:
    def __init__(self, start: int, stop: int, step: int = 1, repeats: int = 1):
        self._start = start
        self._stop = stop
        self._step = step
        self._repeats = repeats
        # поточна позиція та лічильник завершених циклів
        self._current = start
        self._cycle = 0

    def __iter__(self):
        #повертаємо самого себе як ітератор
        return self

    def __next__(self) -> int:
        #якщо всі цикли завершені або діапазон порожній
        if self._cycle >= self._repeats or self._start >= self._stop:
            raise StopIteration

        #зберігаємо поточне значення та переходимо до наступного
        value = self._current
        self._current += self._step

        # якщо дійшли до межі stop, скидаємо на початок і додаємо цикл
        if self._current >= self._stop:
            self._current = self._start
            self._cycle += 1

        return value


def main():
    # базове використання
    print("CyclicRange(1, 4, repeats=3):")
    for num in CyclicRange(1, 4, repeats=3):
        print(num, end=" ")
    print()

    #з кроком
    print("\nCyclicRange(0, 10, step=3, repeats=2):")
    for num in CyclicRange(0, 10, step=3, repeats=2):
        print(num, end=" ")
    print()

    # перетворення на список
    result = list(CyclicRange(5, 8, repeats=2))
    print(f"\nяк список: {result}")

    #обчислення суми елементів через sum()
    total = sum(CyclicRange(1, 5, repeats=2))
    print(f"сума CyclicRange(1, 5, repeats=2): {total}")


if __name__ == "__main__":
    main()