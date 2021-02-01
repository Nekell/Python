class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} started')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, direction):
        print(f'{self.name} turned to {direction}')

    def show_speed(self):
        print(f'Current speed is {self.speed} m/s')


class TownCar(Car):
    def __init__(self):
        self.speed = 60
        self.color = 'grey'
        self.name = 'Town Car'
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print('Attention! Speed level excess!')
        else:
            print(f'Current speed is {self.speed} m/s')


class SportCar(Car):
    def __init__(self):
        self.speed = 120
        self.color = 'yellow'
        self.name = 'Sport Car'
        self.is_police = False


class WorkCar(Car):
    def __init__(self):
        self.speed = 40
        self.color = 'black'
        self.name = 'Work Car'
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print('Attention! Speed level excess!')
        else:
            print(f'Current speed is {self.speed} m/s')


class PoliceCar(Car):
    def __init__(self):
        self.speed = 70
        self.color = 'blue'
        self.name = 'Police Car'
        self.is_police = True
