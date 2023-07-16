import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, one_pay, count):
        if not isinstance(one_pay, (int, float)):
            raise TypeError('Значение стоимости должно быть числом')
        if not isinstance(name, str):
            raise TypeError("Название товара должно быть строкой")
        if not isinstance(count, int):
            raise TypeError("Количество товара должно быть числом")
        self.__name = name
        self.one_pay = one_pay
        self.count = count

        Item.all.append(self)

    def calculate_total_price(self) -> float:
        total_price = self.one_pay * self.count
        return total_price

    def apply_discount(self) -> None:
        Item.price = self.one_pay * Item.pay_rate

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, item):
        if len(item) > 10:
            print('Длина наименования товара превышает 10 символов')
        else:
            self.__name = item

    @staticmethod
    def string_to_number(item):
        if item.isdigit():
            return int(float(item))

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        with open('../src/items.csv', 'r', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                name = item['name']
                price = cls.string_to_number(item['price'])
                count = cls.string_to_number(item['quantity'])
                items = cls(name, price, count)

    def __repr__(self):
        return f"Item('{self.name}', {self.one_pay}, {self.count})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('Складывать можно только объекты класса Item или Phone и дочерние от них.')
        return self.count + other.count



