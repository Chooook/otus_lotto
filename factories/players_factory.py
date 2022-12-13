from entities import Computer, Player
from utils import Validation as Valid


class PlayersFactory:
    @classmethod
    def get_players(cls) -> list[Player | Computer]:
        players_list = []
        players_names = []
        amount = cls._get_players_amount()
        for player_num in range(1, amount + 1):
            print(f'{player_num} игрок:')
            player_type = cls._get_player_type()
            player_args = {'name': cls._get_player_name(players_names)}
            players_names.append(player_args['name'])
            players_list.append(cls._create_player(player_type, player_args))
        return players_list

    @staticmethod
    def _get_players_amount() -> int:
        amount = None
        while not amount:
            amount = input('Введите количество игроков (от 2 до 8):\n')
            try:
                Valid.players_amount(amount)
            except ValueError:
                print('Количество игроков указано неверно!')
                amount = None
        return int(amount)

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

    @staticmethod
    def _get_player_name(players_names) -> str:
        name = None
        while not name:
            name = input('Введите имя игрока:\n')
            try:
                Valid.player_name(name)
            except ValueError:
                print('Имя игрока не может быть пустым!')
                name = None
            if name in players_names:
                print('Такой игрок уже существует!')
                name = None
        return name

    @staticmethod
    def _create_player(_class, kwargs):
        return _class(**kwargs)
