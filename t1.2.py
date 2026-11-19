# завдання 1.2. ітерабельний контейнер StudentGroup з окремим ітератором

from collections import namedtuple

Student = namedtuple("Student", ["name", "grade"])


class StudentGroupIterator:
    def __init__(self, students: list[Student]):
        self._students = students
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Student:
        if self._index >= len(self._students):
            raise StopIteration
        student = self._students[self._index]
        self._index += 1
        return student


class StudentGroup:
    def __init__(self, group_name: str):
        self._group_name = group_name
        self._students: list[Student] = []

    def add_student(self, name: str, grade: int) -> None:
        self._students.append(Student(name, grade))

    def __iter__(self):
        #щоразу повертаємо новий ітератор для багаторазового обходу
        return StudentGroupIterator(self._students)

    def __len__(self) -> int:
        return len(self._students)

    def top_students(self, n: int = 3):
        #сортуємо за оцінкою за спаданням і повертаємо ітератор по перших n
        sorted_students = sorted(self._students, key=lambda s: s.grade, reverse=True)
        return StudentGroupIterator(sorted_students[:n])


def main():
    group = StudentGroup("кі-21")
    group.add_student("олена", 95)
    group.add_student("іван", 78)
    group.add_student("марія", 92)
    group.add_student("петро", 85)
    group.add_student("анна", 88)

    # перший обхід
    print("перший обхід:")
    for student in group:
        print(f"  {student.name}: {student.grade}")

    #другий обхід
    print("\nдругий обхід:")
    for student in group:
        print(f"  {student.name}: {student.grade}")

    #два незалежних ітератори одночасно (вкладений цикл)
    print("\nвсі пари студентів:")
    for s1 in group:
        for s2 in group:
            if s1.name < s2.name:
                print(f"  {s1.name} та {s2.name}")

    #топ-3 студенти за оцінкою
    print("\nтоп-3 студенти:")
    for student in group.top_students(3):
        print(f"  {student.name}: {student.grade}")


if __name__ == "__main__":
    main()s