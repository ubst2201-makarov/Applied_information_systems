# ПИС. Лабораторная работа № 1.
# Группа УБСТ2201
# Выполнил: Макаров В. Е.
# Файл mygroup.py

groupmates = [  # Список студентов
    {
        "name": "Александр",
        "surname": "Романов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Иван",
        "surname": "Иванов",
        "exams": ["История", "АиГ", "КТП", "ПИС"],
        "marks": [5, 5, 4, 4]
    },
    {
        "name": "Валентин",
        "surname": "Макаров",
        "exams": ["ИТиП", "ОС", "УиАИС", "СИИ"],
        "marks": [4, 5, 5, 4]
    },
    {
        "name": "Мария",
        "surname": "Сидорова",
        "exams": ["Информатика", "Математика", "Физика"],
        "marks": [5, 3, 3]
    },
    {
        "name": "Анна",
        "surname": "Павлова",
        "exams": ["Web", "ИС", "КТП"],
        "marks": [4, 4, 4]
    }
]


def print_students(students):  # Функция вывода списка студентов в удобном формате
    for student in students:
        print(f"{student['surname']} {student['name']}")
        print(f"  Средний балл: {sum(student['marks']) / len(student['marks']):.2f}\n")


def filter_students_by_avg(groupm8s, min_avg):  # Функция вывода отфильтрованного списка студентов
    filtered = []
    for student in groupm8s:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > min_avg:
            filtered.append(student)
    return filtered


if __name__ == "__main__":
    try:
        threshold = float(input("Введите минимальный средний балл для фильтрации: "))   # Ввод значения для фильтрации
        if threshold <= 5.00:  # Введённое число должно быть не более 5.00 (поскольку используется пятибалльная шкала)
            selected_students = filter_students_by_avg(groupmates, threshold)   # Вызов функции для получения отфильтрованного списка
            if selected_students:   # Проверка, что выборка не пустая
                print(f"\nСтуденты со средним баллом выше {threshold} \n")
                print_students(selected_students)   # Вызов функции для вывода отфильтрованного списка в удобном формате
            else:
                print(f"\nНет студентов со средним баллом выше {threshold} \n")
        else:
            print("Ошибка: введённое число не должно быть больше 5.00")

    except ValueError:  # Завершение выполнения, если введённое значение - не число
        print("Ошибка: введите число! (При вводе числа с дробью использовать точку в качестве разделителя)")
# Конец кода!