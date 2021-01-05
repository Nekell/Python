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
