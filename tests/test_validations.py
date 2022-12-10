from pytest import mark, param, raises

from validations import num_filter, Validation


@mark.parametrize('num', [
    param('-1', id='negative'),
    param('15', id='too_many'),
    param('a', id='letter'),
])
def test_players_amount_value_error(num):
    with raises(ValueError):
        Validation.players_amount(num)


@mark.parametrize('num', [
    param(['a'], id='list'),
    param({'a': 'a'}, id='dict'),
    param(set('a'), id='set'),
])
def test_players_amount_type_error(num):
    with raises(TypeError):
        Validation.players_amount(num)


@mark.parametrize('_type', [
    param('-1', id='negative'),
    param('15', id='another_num'),
    param('a', id='letter'),
])
def test_player_type_value_error(_type):
    with raises(ValueError):
        Validation.player_type(_type)


@mark.parametrize('_type', [
    param(['a'], id='list'),
    param({'a': 'a'}, id='dict'),
    param(set('a'), id='set'),
])
def test_player_type_type_error(_type):
    with raises(TypeError):
        Validation.player_type(_type)


@mark.parametrize('answer', [
    param('1', id='str_num'),
    param(1, id='int'),
    param('e', id='another_letter'),
    param('у', id='ru_letter'),
    param('Y', id='uppercase'),
    param(['y'], id='list'),
    param({'y': 'y'}, id='dict'),
    param(set('y'), id='set'),
])
def test_answer(answer):
    with raises(ValueError):
        Validation.answer(answer)


@mark.parametrize('el, result', [
    param('1', True, id='str_num'),
    param(1, True, id='int'),
    param('e', False, id='letter'),
])
def test_num_filter(el, result):
    assert num_filter(el) == result


@mark.parametrize('el', [
    param(['a'], id='list'),
    param({'a': 'a'}, id='dict'),
    param(set('a'), id='set'),
])
def test_num_filter(el):
    with raises(TypeError):
        num_filter(el)


def test_player_name():
    with raises(ValueError):
        Validation.player_name('')
