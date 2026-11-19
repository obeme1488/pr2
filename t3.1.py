#завдання 3.1. порівняння list comprehension та generator expression

import sys
import timeit


def memory_comparison():
    #порівняння використання пам'яті
    sizes = [1_000, 10_000, 100_000, 1_000_000]

    print("=" * 60)
    print(f"{'n':>12} | {'list (байт)':>14} | {'gen (байт)':>12} | {'ratio':>8}")
    print("-" * 60)

    for n in sizes:
        data_list = [x ** 2 for x in range(n)]
        data_gen = (x ** 2 for x in range(n))

        list_size = sys.getsizeof(data_list)
        gen_size = sys.getsizeof(data_gen)

        print(f"{n:>12,} | {list_size:>14,} | {gen_size:>12,} | {list_size / gen_size:>7.0f}x")

    print("=" * 60)


def performance_comparison():
    #порівняння продуктивності: sum через list vs generator
    n = 500_000

    time_list = timeit.timeit(
        lambda: sum([x ** 2 for x in range(n)]),
        number=5,
    )

    time_gen = timeit.timeit(
        lambda: sum(x ** 2 for x in range(n)),
        number=5,
    )

    print(f"\nsum() для {n:,} елементів (сумарно за 5 запусків):")
    print(f"  list comprehension: {time_list:.4f} с")
    print(f"  generator expression: {time_gen:.4f} с")
    faster = "list" if time_list < time_gen else "generator"
    print(f"  швидше: {faster}")


def practical_usage():
    # практичні приклади використання generator expression
    words = [
        "python", "ітератор", "генератор", "yield", "comprehension",
        "дані", "пам'ять", "ефективність", "конвеєр", "ліниві",
        "обчислення", "протокол", "об'єкт", "клас", "функція",
    ]

    # найдовше слово через max() + generator expression
    longest = max((w for w in words), key=len)
    print(f"найдовше слово: '{longest}' ({len(longest)} символів)")

    # перевірка, чи всі слова непорожні
    all_nonempty = all(len(w) > 0 for w in words)
    print(f"всі слова непорожні: {all_nonempty}")

    #перевірка, чи є слово довше 15 символів
    has_long = any(len(w) > 15 for w in words)
    print(f"є слово > 15 символів: {has_long}")

    # об'єднання слів у csv-рядок
    csv_line = ",".join(w for w in words)
    print(f"csv: {csv_line}")

    #сума довжин усіх слів
    total_length = sum(len(w) for w in words)
    print(f"сума довжин: {total_length}")

    #словник {слово: довжина} через dict comprehension
    word_lengths = {w: len(w) for w in words}
    print(f"довжини: {word_lengths}")

    numbers = range(1, 101)

    # сума квадратів парних чисел від 1 до 100
    even_squares_sum = sum(x ** 2 for x in numbers if x % 2 == 0)
    print(f"\nсума квадратів парних від 1 до 100: {even_squares_sum}")


def main():
    print(">>> порівняння використання пам'яті <<<\n")
    memory_comparison()

    print("\n>>> порівняння продуктивності <<<")
    performance_comparison()

    print("\n>>> практичне використання generator expression <<<\n")
    practical_usage()


if __name__ == "__main__":
    main()