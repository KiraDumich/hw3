import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, one_pay, count):
        self.__name = name
        self.one_pay = one_pay
        self.count = count
        Item.price = one_pay

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
            self.__name == item[:10]
        else:
            self.__name = item

    @staticmethod
    def string_to_number(item):
        if item.isdigit():
            return int(item)


    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', 'r', encoding='windows-1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for item in reader:
                print(f"{item['name']}, {item['price']}, {item['quantity']}")
                name = item['name']
                price = cls.string_to_number(item['price'])
                quantity = cls.string_to_number(item['quantity'])
                items = cls(name, price, quantity)
                cls.all.append(items)
                print(len(cls.all))



