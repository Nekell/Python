"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Dress(ABC):

    @abstractmethod
    def sum_cloth(self):
        pass


class Coat(Dress):
    def __init__(self, v: float):
        self.v = v

    @property
    def sum_cloth(self):
        answer = self.v / 6.5 + 0.5
        return round(answer, 3)


class Suit(Dress):
    def __init__(self, h: float):
        self.h = h

    @property
    def sum_cloth(self):
        answer = self.h * 2 + 0.3
        return answer


some_coat = Coat(float(input("Enter coat size: ")))
print(some_coat.sum_cloth, "meters required")
some_suit = Suit(float(input("Enter your height: ")))
print(some_suit.sum_cloth, "meters required")
