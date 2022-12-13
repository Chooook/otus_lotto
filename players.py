from card import Card
from validations import Validation as Valid


class Player:
    def __init__(self, name):
        self.name = name
        self.card = Card(self)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, card={self.card}'

    def ask(self, num) -> bool:
        answer = None
        while not answer:
            answer = input(f'Закрыть номер {num}?\n'
                           'y - да, n - нет:\n')
            try:
                Valid.answer(answer)
            except ValueError:
                print('Варианты ответа: "y" и "n"')
                answer = None
        if answer == 'y':
            return True
        return False


class Computer(Player):
    def __repr__(self):
        return f'Computer(name={self.name}, card={self.card}'

    def ask(self, num) -> bool:
        if num in self.card:
            return True
        return False


class PlayersMaker:
    # TODO: сборщик игроков для вынесения сборки в отдельный модуль из Game
    pass
