from .fixtures import bag


def test_bag_get_barrel(bag):
    assert bag._nums_list[0] == bag.get_barrel()
