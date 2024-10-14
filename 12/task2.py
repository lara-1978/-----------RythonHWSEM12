# Задача 2. Класс с валидацией данных
# Создайте класс Person, который имеет атрибуты name, age, и email. При
# установке значения атрибута name, оно должно начинаться с заглавной буквы.
# При установке значения атрибута age, оно должно быть целым числом в
# диапазоне от 0 до 120. При установке значения атрибута email, оно должно
# содержать символ @.
# Подсказка № 1
# Используйте метод __setattr__ для валидации установки атрибутов. Этот метод
# позволяет вам перехватывать присвоение значений атрибутам класса, что удобно для
# реализации проверки корректности значений.


class Person:
    def __setattr__(self, name, value):
        if name == 'name':
            if not (value and value[0].isupper() and value.isalpha()):
                raise ValueError("Имя должно начинаться с заглавной буквы и состоять из букв")
        elif name == 'age':
            if not (isinstance(value, int) and 0 <= value <= 120):
                raise ValueError("Возраст должен быть целым числом от 0 до 120")
            elif name == 'email':
                if '@' not in value:
                    raise ValueError("Электронная почта должна содержать символ '@'")
                    super().__setattr__(name, value)
        def __str__(self):
            return f"Person(name={self.name}, age={self.age}, email={self.email})"
    # Пример использования
try:
    p = Person()
    p.name = "John"
    p.age = 25
    p.email = "john@example.com"
    print(p)
except ValueError as e:
    print(e)







