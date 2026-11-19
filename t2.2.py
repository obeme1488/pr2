# завдання 2.2. конвеєр генераторів для обробки даних про оцінки студентів

from collections import defaultdict


SAMPLE_DATA = [
    "олена,математика,95",
    "іван,математика,78",
    "",
    "марія,фізика,92",
    "петро,математика,INVALID",
    "анна,фізика,88",
    "олена,фізика,90",
    "іван,програмування,85",
    "марія,програмування,91",
    "петро,фізика,76",
    "анна,математика,93",
    "олена,програмування,97",
    "",
    "марія,математика,89",
    "іван,фізика,72",
    "петро,програмування,80",
    "анна,програмування,86",
]


def data_source(records: list[str]):
    #Eтап 1: видаємо записи по одному
    for record in records:
        yield record


def filter_empty(records):
    #етап 2: пропускаємо порожні рядки
    for record in records:
        if record.strip():
            yield record


def parse_records(records):
    #етап 3: розбиваємо рядок і перетворюємо оцінку на int
    for record in records:
        parts = record.split(",")
        if len(parts) != 3:
            continue
        student, subject, grade_str = parts
        try:
            grade = int(grade_str.strip())
        except ValueError:
            # пропускаємо записи з некоректною оцінкою
            continue
        yield {
            "student": student.strip(),
            "subject": subject.strip(),
            "grade": grade,
        }


def filter_passed(records, min_grade: int = 60):
    # етап 4: залишаємо лише оцінки не нижче min_grade
    for record in records:
        if record["grade"] >= min_grade:
            yield record


def format_output(records):
    #етап 5: формуємо рядок для виводу
    for record in records:
        yield f"[{record['subject']}] {record['student']}: {record['grade']} балів"


def main():
    # конвеєр 1: відфільтрований вивід (>= 75 балів)
    pipeline = format_output(
        filter_passed(
            parse_records(
                filter_empty(
                    data_source(SAMPLE_DATA)
                )
            ),
            min_grade=75,
        )
    )

    print("=== результати (>= 75 балів) ===")
    for line in pipeline:
        print(line)

    #конвеєр 2: обчислення середнього балу по предметах
    print("\n=== середній бал по предметах ===")
    subject_grades = defaultdict(list)
    for record in parse_records(filter_empty(data_source(SAMPLE_DATA))):
        subject_grades[record["subject"]].append(record["grade"])

    for subject, grades in sorted(subject_grades.items()):
        avg = sum(grades) / len(grades)
        print(f"  {subject}: {avg:.1f} (з {len(grades)} оцінок)")


if __name__ == "__main__":
    main()