from __future__ import annotations

import sys

from bag import Bag
from players import Computer, Player
from validations import Validation as Valid


class Game:
    def __init__(self):
        self._players_list = []
        self.bag = Bag()

    def start(self):
        self._players_list = self._get_players(self._get_players_amount())
        print(f'{"-" * 35}\nИгра начинается!!!\n{"-" * 35}')
        self._turn()

    @classmethod
    def _get_players_amount(cls) -> int:
        amount = None
        while not amount:
            amount = input('Введите количество игроков (от 2 до 8):\n')
            try:
                Valid.players_amount(amount)
            except ValueError:
                print('Количество игроков указано неверно!')
                amount = None
        return int(amount)

    def _get_players(self, amount) -> list[Player | Computer]:
        players = []
        for player_num in range(1, amount + 1):
            print(f'{player_num} игрок:')
            player_type = self._get_player_type()
            player_args = {'name': self._get_player_name()}
            players.append(self._create_player(player_type, player_args))
        return players

    @staticmethod
    def _get_player_type() -> type[Player] | type[Computer]:
        _type = None
        while not _type:
            _type = input('Введите тип игрока:\n'
                          '1 - человек, 2 - компьютер\n')
            try:
                Valid.player_type(_type)
            except ValueError:
                print('Тип игрока указан неверно!')
                _type = None
        match int(_type):
            case 1:
                return Player
            case 2:
                return Computer

    def _get_player_name(self) -> str:
        name = None
        while not name:
            name = input('Введите имя игрока:\n')
            try:
                Valid.player_name(name)
            except ValueError:
                print('Имя игрока не может быть пустым!')
                name = None
            if name in self._players_list:
                print('Такой игрок уже существует!')
                name = None
        return name

    @staticmethod
    def _create_player(_class, kwargs):
        return _class(**kwargs)

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


if __name__ == '__main__':
    game = Game()
    game.start()
