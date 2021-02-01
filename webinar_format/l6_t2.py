class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_sum_mass(self):
        mass = 25
        height = 5
        sum_mass = self._length * self._width * mass * height
        return sum_mass


road = Road(5000, 20)
print(road.calc_sum_mass())
