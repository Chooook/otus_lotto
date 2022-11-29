class Validation:
    @staticmethod
    def players_amount(num):
        try:
            num = int(num)
            if 2 <= num <= 8:
                return True
            raise ValueError
        except ValueError:
            print('Количество игроков указано неверно!')
            return False

    @staticmethod
    def player_type(_type):
        try:
            _type = int(_type)
            if _type == 1 or _type == 2:
                return True
            raise ValueError
        except ValueError:
            print('Тип игрока указан неверно!')
            return False

    @staticmethod
    def answer(answer):
        if answer == 'y' or answer == 'n':
            return True
        print('Варианты ответа: "y" и "n"')
        return False
