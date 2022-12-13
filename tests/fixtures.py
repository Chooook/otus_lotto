from pytest import fixture

from entities import Bag


@fixture()
def bag():
    return Bag()
