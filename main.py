from __future__ import annotations

import sys

from entities import Bag
from factories.players_factory import PlayersFactory


class Game:
    def __init__(self):
        self._players_list = []
        self.bag = Bag()

    def start(self):
        self._players_list = PlayersFactory.get_players()
        print(f'{"-" * 35}\nИгра начинается!!!\n{"-" * 35}')
        self._turn()

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
                      f'Игрок {player}\n'
                      f'Попытался закрыть число {num}!\n'
                      f'Этого числа нет на его карточке!\n'
                      f'{"-" * 35}\n'
                      f'Игрок {player} проиграл!\n'
                      f'Игра окончена!!!'
                      f'\n{"-" * 35}')
                sys.exit()
            else:
                print(f'{"-" * 35}\n'
                      f'Игрок {player}\n'
                      f'Не попытался закрыть число {num}!\n'
                      f'Это число есть на его карточке!\n'
                      f'{"-" * 35}\n'
                      f'Игрок {player} проиграл!\n'
                      f'Игра окончена!\n'
                      f'{"-" * 35}')
                sys.exit()


if __name__ == '__main__':
    game = Game()
    game.start()
