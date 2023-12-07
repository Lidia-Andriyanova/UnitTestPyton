""" Tests for compare averages of two lists """
import pytest
from task import ListAvgCompare


@pytest.mark.parametrize('first_list, second_list, result', [
    ([10, 20, 30], [4, 5, 9, 10], 'Первый список имеет большее среднее значение'),
    ([1, 8, 25, 17, -9], [-1, 104, 232], 'Второй список имеет большее среднее значение'),
    ([5, 10, 15], [20, 0, -10, 35, 5], 'Средние значения равны')
])
def test_compare_lists(first_list, second_list, result):
    """ Compare number lists """
    list_compare = ListAvgCompare(first_list, second_list)
    assert list_compare.compare_avg() == result


@pytest.mark.parametrize('first_list, second_list', [
    ('Not a list', [4, 5, 9, 10]),
    ([1, 8, 25, 17, -9], 'Not a list'),
    (['10', '20', '30'], [4, 5, 9, 10]),
    ([10, 20, 30], ['4', '5', '9', '10'])
])
def test_compare_typeerror(first_list, second_list):
    """ Compare not a list list argument and not a number list """
    list_compare = ListAvgCompare(first_list, second_list)
    with pytest.raises(TypeError):
        list_compare.compare_avg()


@pytest.mark.parametrize('first_list, second_list, result', [
    ([], [4, 5, 9, 10], 'Второй список имеет большее среднее значение'),
    ([1, -8, -25, -17, -9], [], 'Второй список имеет большее среднее значение'),
    ([], [], 'Средние значения равны')
])
def test_compare_empty_list(first_list, second_list, result):
    """ Compare empty lists """
    list_compare = ListAvgCompare(first_list, second_list)
    assert list_compare.compare_avg() == result
