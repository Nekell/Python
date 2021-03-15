"""
2. Реализовать класс Road (дорога), в котором определить атрибуты:
length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта,
необходимого для покрытия всего дорожного полотна.
Использовать формулу:
длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_sum_mass(self, mass, height):
        sum_mass = self._length * self._width * mass * height
        return sum_mass


road_length = int(input("Enter the length of the road: "))
road_width = int(input("Enter the width of the road: "))
road = Road(road_length, road_width)
road_mass = int(input("Enter the mass of asphalt to cover one square meter of the road with 1 cm thick asphalt: "))
road_height = int(input("Enter the thickness of the roadbed: "))
print(road.calc_sum_mass(road_mass, road_height), "kg")
