from utils import num_filter


class Card:
    def __init__(self, line1, line2, line3, player=None):
        self.player = player
        self.line1 = line1
        self.line2 = line2
        self.line3 = line3

    def __str__(self):
        first_row = '------------ Карточка -------------'
        if self.player:
            # TODO: добавить подсчет "-" символов до и после имени
            first_row = f'--- Карточка игрока {self.player} ---'
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

    def check_lines(self) -> bool:
        # TODO: test it
        return not (list(filter(num_filter, self.line1)) and
                    list(filter(num_filter, self.line2)) and
                    list(filter(num_filter, self.line3)))

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
