# Задание 1. Работа с данными студентов
# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только
# букв. Если ФИО не соответствует условию, выведите:
# ФИО должно состоять только из букв и начинаться с заглавной буквы
# ○ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы. Если такого предмета нет, выведите:
# Предмет {Название предмета} не найден
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до
# 100). В противном случае выведите:
# Оценка должна быть целым числом от 2 до 5
# Результат теста должен быть целым числом от 0 до 100
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по
# оценкам всех предметов вместе взятых.
# Вам предоставлен файл subjects.csv, содержащий предметы. Сейчас в файл записана
# следующая информация.
# Математика,Физика,История,Литература
# Создайте класс Student, который будет представлять студента и его успехи по
# предметам. Класс должен иметь следующие методы:
# Атрибуты класса:
# name (str): ФИО студента. subjects (dict): Словарь, который хранит предметы в
# качестве ключей и информацию об оценках и результатах тестов для каждого предмета в
# виде словаря.
# Магические методы (Dunder-методы):
# __init__(self, name, subjects_file): Конструктор класса. Принимает имя студента
# и файл с предметами и их результатами. Инициализирует атрибуты name и subjects и
# вызывает метод load_subjects для загрузки предметов из файла.
# __setattr__(self, name, value): Дескриптор, который проверяет установку атрибута
# name. Убеждается, что name начинается с заглавной буквы и состоит только из букв.
# __getattr__(self, name): Позволяет получать значения атрибутов предметов (оценок
# и результатов тестов) по их именам.
# __str__(self): Возвращает строковое представление студента, включая имя и список
# предметов.
# Студент: Иван Иванов
# Предметы: Математика, История
# Методы класса:
# load_subjects(self, subjects_file): Загружает предметы из файла CSV.
# Использует модуль csv для чтения данных из файла и добавляет предметы в атрибут
# subjects.
# add_grade(self, subject, grade): Добавляет оценку по заданному предмету.
# Убеждается, что оценка является целым числом от 2 до 5.
# add_test_score(self, subject, test_score): Добавляет результат теста по
# заданному предмету. Убеждается, что результат теста является целым числом от 0 до 100.
# get_average_test_score(self, subject): Возвращает средний балл по тестам для
# заданного предмета.
# get_average_grade(self): Возвращает средний балл по всем предметам.

import csv


class NameDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    # def __set__(self, instance, value):
    #     if not isinstance(value, str) or not value.isalpha() or not value[0].isupper():
    #         raise ValueError('ФИО должно состоять только из букв и начинаться с заглавной буквы')
    #     instance.__dict__[self.name] = value


class Student:
    name = NameDescriptor()

    def __init__(self, name, subjects_file):
        self.name = name
        self.subjects = {}
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):

        with open(subjects_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            subjects = next(reader)
            for subject in subjects:
                self.subjects[subject] = {'grades': [], 'test_scores': []}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            print(f'Предмет {subject} не найден')
            return
        if not (isinstance(grade, int) and 2 <= grade <= 5):
            raise ValueError('Оценка должна быть целым числом от 2 до 5')
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self, subject, test_score):
        if subject not in self.subjects:
            print(f'Предмет {subject} не найден')
            return
        if not (isinstance(test_score, int) and 0 <= test_score <= 100):
            raise ValueError('Результат теста должен быть целым числом от 0 до 100')
        self.subjects[subject]['test_scores'].append(test_score)

    def get_average_test_score(self, subject):
        if subject not in self.subjects or not self.subjects[subject]['test_scores']:
            return 0
        return sum(self.subjects[subject]['test_scores']) / len(self.subjects[subject]['test_scores'])

    def get_average_grade(self):
        all_grades = [grade for subject in self.subjects.values() for grade in subject['grades']]
        if not all_grades:
            return 0
        return sum(all_grades) / len(all_grades)

    def __str__(self):
        subjects_list = ', '.join(self.subjects.keys())
        return f'Студент: {self.name}\nПредметы: {subjects_list}'

try:
    with open("subjects.csv", mode='w', encoding='utf-8') as file:
        file.write("Математика,Физика,История,Литература\n")
    print("Файл subjects.csv успешно создан.")
except Exception as e:
    print(f"Ошибка при создании файла: {e}")

try:
    student = Student("Иван Иванов", "subjects.csv")
    student.add_grade("Математика", 4)
    student.add_test_score("Математика", 85)
    student.add_grade("История", 5)
    student.add_test_score("История", 90)
    print(student)
    print(f'Средний балл по тестам по предмету "Математика": {student.get_average_test_score("Математика")}')
    print(f'Средний балл по всем предметам: {student.get_average_grade()}')
except ValueError as e:
    print(e)
