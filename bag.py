from random import shuffle

from numbers_dict import NUMS_DICT


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

    def get_barrel(self) -> int:
        barrel = self._nums_list.pop(0)
        try:
            text = NUMS_DICT[str(barrel)]
        except KeyError:
            text = f'Бочонок номер {barrel}!\n{"-" * 35}\n{self}\n{"-" * 35}'
        else:
            text = f'{text}! {barrel}\n{"-" * 35}\n{self}\n{"-" * 35}'
        print(text)
        return barrel
