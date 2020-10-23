"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. 
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.
"""
class Сlothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def square_c(self):
        return self.size / 6.5 + 0.5

    def square_s(self):
        return self.height * 0.2 + 0.3

    @property
    def square_full(self):
        return round((coat.size / 6.5 + 0.5) + (suit.height * 2 + 0.3), 2)


class Coat(Сlothes):
    def __init__(self, size, height):
        Сlothes.__init__(size, height)
        self.square_c = round((self.size / 6.5 + 0.5), 2)

    def __str__(self):
        return f'{self.square_c}'


class Suit(Сlothes):
    def __init__(self, size, height):
        Сlothes.__init__(size, height)
        self.square_s = round((self.height * 2 + 0.3), 2)

    def __str__(self):
        return f'{self.square_s}'

#print(suit.square_full)




