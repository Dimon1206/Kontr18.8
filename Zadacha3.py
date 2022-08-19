class Tomato:

    states = {0: 'Ничего', 1: 'Цветок', 2: 'Зеленый томат', 3: 'Красный томат'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False


    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Помидор {self._index} сейчас {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовник ухаживает за помидорами...')
        self._plant.grow_all()
        print('Садовник окончил работу')

    def harvest(self):
        print('Садовник убирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Сбор уражая окончен')
        else:
            print('Раньше времени. Помидоры еще не созрели.')


    @staticmethod
    def knowledge_base():
        print('''Время снятия помидор с куста зависит от того, 
как именно будет использоваться урожай. Если плоды сразу же будут употребляться в пищу,
их срывают на этапе биологической зрелости, то есть когда они полностью поспеют и покраснеют..''')


if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Анатолий', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()