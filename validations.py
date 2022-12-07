class Validation:
    @staticmethod
    def players_amount(num):
        num = int(num)
        if not (2 <= num <= 8):
            raise ValueError

    @staticmethod
    def player_type(_type):
        _type = int(_type)
        if _type != 1 and _type != 2:
            raise ValueError

    @staticmethod
    def answer(answer):
        if answer != 'y' and answer != 'n':
            raise ValueError


def num_filter(el):
    try:
        int(el)
        return True
    except ValueError:
        return False
