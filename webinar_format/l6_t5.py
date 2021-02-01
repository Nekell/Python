class Stationery:
    title = 'Stationery'

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        print(f'Start drawing by {self.title}')


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        print(f'Start drawing by {self.title}')


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        print(f'Start drawing by {self.title}')