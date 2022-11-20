from random import shuffle
import sys

from numbers_dict import NUMS_DICT
from validations import Validation as Valid


class Game:
    def __init__(self):
        self._players_list = self._create_players(
            int(self._get_players_amount())
        )
        self.bag = Bag()

    def start(self):
        print(f'{"-"*35}\nИгра начинается!!!\n{"-"*35}')
        self._turn()

    @classmethod
    def _get_players_amount(cls):
        amount = input('Введите количество игроков (от 2 до 8):\n')
        return Valid.players_amount(amount, cls._get_players_amount)

    @classmethod
    def _create_players(cls, amount):
        players = []
        for player_num in range(1, amount + 1):
            print(f'{player_num} игрок:')
            player_type = cls._get_player_type()
            players.append(cls._create_player(player_type, player_num))
        return players

    @classmethod
    def _get_player_type(cls):
        _type = input('Введите тип игрока:\n'
                      '1 - человек, 2 - компьютер\n')
        return Valid.player_type(_type, cls._get_player_type)

    @staticmethod
    def _create_player(player_type, player_num):
        match player_type:
            case 1:
                player_name = f'{player_num} - Человек'
                return Person(player_name)
            case 2:
                player_name = f'{player_num} - Компьютер'
                return Computer(player_name)

    def _turn(self):
        num = self.bag.get_barrel()
        self._check_cards(num)
        self._turn()

    def _check_cards(self, num):
        for player in self._players_list:
            player.check_card(num)


class Bag:
    def __init__(self):
        self._nums_list = list(range(1, 91))
        shuffle(self._nums_list)

    def __str__(self):
        prefix = 'Осталось'
        postfix = 'бочонков'
        match len(self) % 10:
            case 1:
                prefix = 'Остался'
                postfix = 'бочонок'
            case 2 | 3 | 4:
                postfix = 'бочонка'
        return f'{prefix} {len(self)} {postfix}'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._nums_list)

    def get_barrel(self):
        barrel = self._nums_list.pop(0)
        try:
            text = NUMS_DICT[str(barrel)]
            text = f'{text}! {barrel}\n{"-"*35}\n{self}\n{"-"*35}'
        except KeyError:
            text = f'Бочонок номер {barrel}!\n{"-"*35}\n{self}\n{"-"*35}'
        print(text)
        return barrel


class Player:
    def __init__(self, name):
        self.name = name
        self.card = Card(self)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Player(name={self.name}, card={self.card}'


class Person(Player):
    def __repr__(self):
        return f'Person(name={self.name}, card={self.card}'

    def check_card(self, num):
        print(self.card)
        if self._ask():
            self.card.del_num(num)
        elif self.card.check(num):
            print(f'{"-"*35}\n'
                  f'Игрок {self.name} не попытался закрыть {num}!\n'
                  f'Это число есть на его карточке!\n'
                  f'{"-"*35}\n'
                  f'Игрок {self.name} проиграл! Игра окончена!\n'
                  f'{"-"*35}')
            sys.exit()

    @classmethod
    def _ask(cls):
        answer = input('Закрыть номер?\n'
                       'y - да, n - нет:\n')
        return Valid.answer(answer, cls._ask)


class Computer(Player):
    def __repr__(self):
        return f'Computer(name={self.name}, card={self.card}'

    def check_card(self, num):
        if self.card.check(num):
            self.card.del_num(num)


class Card:
    def __init__(self, player):
        self.player = player
        self._nums = list(range(1, 91))
        shuffle(self._nums)
        self.line1 = sorted(self._nums[:5])
        self.line2 = sorted(self._nums[5:10])
        self.line3 = sorted(self._nums[10:15])

    def __str__(self):
        first_row = '------------ Карточка -------------'
        if isinstance(self.player, Person):
            first_row = f'--- Карточка игрока {self.player} ---'
        if isinstance(self.player, Computer):
            first_row = f'-- Карточка игрока {self.player} --'
        line1 = [' ' + str(i) if i // 10 == 0 else str(i) for i in self.line1]
        line2 = [' ' + str(i) if i // 10 == 0 else str(i) for i in self.line2]
        line3 = [' ' + str(i) if i // 10 == 0 else str(i) for i in self.line3]
        return (f'{first_row}\n'
                f'{"      ".join(line1)}\n'
                f'{"      ".join(line2)}\n'
                f'{"      ".join(line3)}\n'
                f'{"-" * 35}')

    def __repr__(self):
        return (f'Card(player={self.player}, '
                f'line1={self.line1}, '
                f'line2={self.line2}, '
                f'line3={self.line3})')

    def check(self, num):
        if num in self.line1:
            return True
        if num in self.line2:
            return True
        if num in self.line3:
            return True

    def check_lines(self):
        if (len(self.line1) == 0
                or len(self.line2) == 0
                or len(self.line3) == 0):
            print(f'Игрок {self.player} победил!')
            sys.exit()

    def del_num(self, num):
        line = None
        if num in self.line1:
            self.line1.remove(num)
            line = 'линии 1'
        elif num in self.line2:
            self.line2.remove(num)
            line = 'линии 2'
        elif num in self.line3:
            self.line3.remove(num)
            line = 'линии 3'
        if line:
            print(f'Игрок {self.player} закрыл {num} на {line}!\n{self}')
            self.check_lines()
        else:
            print(f'{"-"*35}\n'
                  f'Игрок {self.player} попытался закрыть {num}!\n'
                  f'Этого числа нет на его карточке!\n'
                  f'{"-"*35}\n'
                  f'Игрок {self.player} проиграл! Игра окончена!!!'
                  f'\n{"-"*35}')
            sys.exit()


if __name__ == '__main__':
    game = Game()
    game.start()
