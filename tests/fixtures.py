from pytest import fixture

from main import Bag


@fixture()
def bag():
    return Bag()
