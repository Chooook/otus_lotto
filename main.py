from random import shuffle
import sys

from numbers_dict import NUMS_DICT
from validations import Validation as Valid


class Game:
    def __init__(self):
        self._players_list = self._get_players(self._get_players_amount())
        self.bag = Bag()

    def start(self):
        print(f'{"-" * 35}\nИгра начинается!!!\n{"-" * 35}')
        self._turn()

    @classmethod
    def _get_players_amount(cls):
        amount = input('Введите количество игроков (от 2 до 8):\n')
        if Valid.players_amount(amount):
            return int(amount)
        cls._get_players_amount()

    @classmethod
    def _get_players(cls, amount):
        players = []
        for player_num in range(1, amount + 1):
            print(f'{player_num} игрок:')
            player_type = int(cls._get_player_type())
            players.append(cls._create_player(player_type, player_num))
        return players

    @classmethod
    def _get_player_type(cls):
        _type = input('Введите тип игрока:\n'
                      '1 - человек, 2 - компьютер\n')
        if Valid.player_type(_type):
            return _type
        cls._get_player_type()

    @staticmethod
    def _create_player(player_type, player_num):
        match player_type:
            case 1:
                player_name = f'{player_num} - Человек'
                return Player(player_name)
            case 2:
                player_name = f'{player_num} - Компьютер'
                return Computer(player_name)

    def _turn(self):
        num = self.bag.get_barrel()
        self._check_cards(num)
        for player in self._players_list:
            if player.card.check_lines():
                self._end_game(player, win=True)
        self._turn()

    def _check_cards(self, num):
        for player in self._players_list:
            print(player.card)
            answer = player.ask(num)
            match answer, num in player.card:
                case True, True:
                    player.card.del_num(num)
                    continue
                case False, False:
                    continue
            self._end_game(player, wrong_answer=answer, num=num)

    @staticmethod
    def _end_game(player, win=False, wrong_answer=None, num=None):
        if win:
            print(f'Игрок {player} победил!')
            sys.exit()
        if wrong_answer is not None:
            if wrong_answer:
                print(f'{"-" * 35}\n'
                      f'Игрок {player} попытался закрыть число {num}!\n'
                      f'Этого числа нет на его карточке!\n'
                      f'{"-" * 35}\n'
                      f'Игрок {player} проиграл! Игра окончена!!!'
                      f'\n{"-" * 35}')
                sys.exit()
            else:
                print(f'{"-" * 35}\n'
                      f'Игрок {player} не попытался закрыть число {num}!\n'
                      f'Это число есть на его карточке!\n'
                      f'{"-" * 35}\n'
                      f'Игрок {player} проиграл! Игра окончена!\n'
                      f'{"-" * 35}')
                sys.exit()


class Bag:
    def __init__(self):
        self._nums_list = list(range(1, 91))
        shuffle(self._nums_list)

    def __str__(self):
        prefix = 'Осталось'
        postfix = 'бочонков'
        if len(self) != 11 | 12 | 13 | 14:
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
        # TODO: test it
        barrel = self._nums_list.pop(0)
        try:
            text = NUMS_DICT[str(barrel)]
            text = f'{text}! {barrel}\n{"-" * 35}\n{self}\n{"-" * 35}'
        except KeyError:
            text = f'Бочонок номер {barrel}!\n{"-" * 35}\n{self}\n{"-" * 35}'
        print(text)
        return barrel


class Player:
    def __init__(self, name):
        self.name = name
        self.card = Card(self)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, card={self.card}'

    def ask(self, num):
        answer = input(f'Закрыть номер {num}?\n'
                       'y - да, n - нет:\n')
        if Valid.answer(answer):
            if answer == 'y':
                return True
            return False
        self.ask(num)


class Computer(Player):
    def __repr__(self):
        return f'Computer(name={self.name}, card={self.card}'

    def ask(self, num):
        if num in self.card:
            return True
        return False


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
        if isinstance(self.player, Player):
            first_row = f'--- Карточка игрока {self.player} ---'
        if isinstance(self.player, Computer):
            first_row = f'-- Карточка игрока {self.player} --'
        line1 = [' ' + i if len(i) < 2 else i for i in map(str, self.line1)]
        line2 = [' ' + i if len(i) < 2 else i for i in map(str, self.line2)]
        line3 = [' ' + i if len(i) < 2 else i for i in map(str, self.line3)]
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

    def __contains__(self, item):
        if item in self.line1:
            return True
        if item in self.line2:
            return True
        if item in self.line3:
            return True

    def check_lines(self):
        # TODO: test it
        return (not self.line1
                or not self.line2
                or not self.line3)

    def del_num(self, num):
        line = None
        if num in self.line1:
            self.line1[self.line1.index(num)] = '--'
            line = 'линии 1'
        elif num in self.line2:
            self.line2[self.line2.index(num)] = '--'
            line = 'линии 2'
        elif num in self.line3:
            self.line3[self.line3.index(num)] = '--'
            line = 'линии 3'
        if line:
            print(f'Игрок {self.player} закрыл {num} на {line}!\n{self}')


if __name__ == '__main__':
    game = Game()
    game.start()
