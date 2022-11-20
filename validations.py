class Validation:
    @staticmethod
    def players_amount(num, func):
        try:
            num = int(num)
            if 2 <= num <= 8:
                return num
            raise ValueError
        except ValueError:
            print('Количество игроков указано неверно!')
            return func()

    @staticmethod
    def player_type(_type, func):
        try:
            _type = int(_type)
            if _type == 1 or _type == 2:
                return _type
            raise ValueError
        except ValueError:
            print('Тип игрока указан неверно!')
            return func()

    @staticmethod
    def answer(answer, func):
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print('Варианты ответа: "y" и "n"')
            return func()
