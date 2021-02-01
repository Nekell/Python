class Worker:
    name = 'Ivan'
    surname = 'Petrov'
    position = 'Engineer'
    _income = {'wage': 100500,
               'bonus': 10000}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']
