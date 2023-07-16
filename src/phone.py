from src.item import Item


class Phone(Item):

    def __init__(self, name, one_pay, count, number_of_sim):
        super().__init__(name, one_pay, count)
        if number_of_sim > 0 and isinstance(number_of_sim, int):
            self.number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.one_pay}, {self.count}, {self.number_of_sim})"

    def __str__(self):
        return self.name
