# Задача 4. Класс с контролем цены и количества
# Создайте класс Product с атрибутами name, price, и quantity. price должен
# быть положительным числом, а quantity неотрицательным целым числом. При
# попытке установить price или quantity, должен производиться контроль значений.
#   Подсказка № 1
# Используйте метод __setattr__ для контроля значений атрибутов. Переопределите
# метод __setattr__, чтобы проверять, что price является положительным числом, а
# quantity — неотрицательным целым числом, прежде чем устанавливать значение атрибутов.
#   Подсказка № 2
# Проверьте тип и значение для price. Убедитесь, что price является либо целым
# числом, либо числом с плавающей точкой, и что оно больше нуля.
#   Подсказка № 3
# Проверьте тип и значение для quantity. Убедитесь, что quantity является целым
# числом и не отрицательным.
#   Подсказка № 4
# Используйте метод super().__setattr__ для установки атрибутов после проверки.
# Вызовите метод super().__setattr__ для фактического присвоения значений атрибутам после проверки.


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price  # Вызов __setattr__ здесь не сработает
        self.quantity = quantity  # Вызов __setattr__ здесь не сработает

    def __setattr__(self, name, value):
        if name == 'price':
            if not (isinstance(value, (int, float)) and value > 0):
                raise ValueError('price должен быть положительным числом')
        elif name == 'quantity':
            if not (isinstance(value, int) and value >= 0):
                raise ValueError('quantity должно быть неотрицательным целым числом')

        super().__setattr__(name, value)

    def __str__(self):
        return f'Product(name={self.name}, price={self.price}, quantity={self.quantity})'

try:
    prod = Product("Laptop", 1000, 10)  # если сделать  -10, то будет 'quantity должно быть неотрицательным целым числом"
    prod.price = 1200
    prod.quantity = 5
    print(prod)
except ValueError as e:
    print(e)





