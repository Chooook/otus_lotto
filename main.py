from dataclasses import dataclass
from random import shuffle
import sys

from numbers_dict import NUMS_DICT


class Host:
    _nums_list = list(range(1, 91))
    shuffle(_nums_list)
    _players_list = []

    def play(self):
        print('Начинаем нашу игру!')
        self._create_players(self._get_players_amount())
        while 1 == 1:
            self._ask()
            self._next_round()

    @staticmethod
    def _get_players_amount():
        amount = input('Введите количество игроков (от 2 до 8): ')
        return Host._players_amount_validation(amount)

    @staticmethod
    def _players_amount_validation(num):
        try:
            num = int(num)
            if 2 <= num <= 8:
                return num
            raise ValueError
        except ValueError:
            print('Количество игроков указано неверно!')
            return Host._get_players_amount()

    def _create_players(self, amount):
        for player in range(1, int(amount) + 1):
            self._players_list.append(
                Player(
                    input(f'Введите тип {player} игрока\n'
                          '1 - человек, 2 - компьютер\n'),
                    input('Введите имя игрока: ')
                )
            )

    def _next_round(self):
        num = self._nums_list.pop(0)
        num_name = NUMS_DICT.get(str(num))
        message = f'{num_name}! {num}' if num_name else f'{num}!'
        print(message)
        for player in self._players_list:
            player.check_cards(num)

    def _ask(self):
        answer = input('Нажмите клавишу `Enter`, чтобы продолжить игру.\n'
                       'Введите 1, чтобы просмотреть оставшиеся числа.')
        if answer:
            if answer == '1':
                print(self._nums_list)
                self._ask()
            else:
                self._ask()


class Player:
    def __init__(
            self,
            _type: str,
            name: str,
    ):
        self._type = 'Компьютер' if _type == '2' else 'Человек'
        self.name = name
        self._cards = self._get_cards()

    def __repr__(self):
        return f'{self._type}: {self.name}'

    @staticmethod
    def _get_cards():
        return [Card() for _ in range(3)]

    def check_cards(self, num):
        for card in self._cards:
            card.check(num, self)


@dataclass
class Card:
    _nums = list(range(1, 91))

    def __post_init__(self):
        self._create()

    def __repr__(self):
        return (f'{self.lines[0]}\n'
                f'{self.lines[1]}\n'
                f'{self.lines[2]}\n')

    def _create(self):
        shuffle(self._nums)
        self._line1 = self._nums[:5]
        self._line2 = self._nums[5:10]
        self._line3 = self._nums[10:15]
        self.lines = [self._line1, self._line2, self._line3]

    def check(self, number, player):
        for i, line in zip([1, 2, 3], self.lines):
            if number in line:
                line.remove(number)
                print(f'Игрок {player} закрыл число {number}\n'
                      f'Оставшиеся значения {i} линии :\n{line}')
                if len(line) == 0:
                    print(f'Игрок {player} победил!\n'
                          'ИГРА ОКОНЧЕНА!')
                    sys.exit()


if __name__ == '__main__':
    game = Host()
    game.play()
