from random import shuffle

from entities.card import Card


class CardFactory:
    @staticmethod
    def get_card(player):
        nums = list(range(1, 91))
        shuffle(nums)
        line1 = sorted(nums[:5])
        line2 = sorted(nums[5:10])
        line3 = sorted(nums[10:15])
        return Card(line1, line2, line3, player)
