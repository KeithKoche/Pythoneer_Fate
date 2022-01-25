import pytest


@pytest.mark.smoke
@pytest.mark.parametrize(("a", "b"), [(1, 2), (2, 3), (3, 4)])
def test_dz1(set_array_a, a, b):
    a = 1
    b = 2
    assert a + b == 3


@pytest.mark.regression
def test_dz2(set_array_a, set_array_b):
    assert set_array_a - set_array_b == -1


@pytest.mark.regression
def test_dz3(num_one):
    a = 1
    b = 2
    assert a * b * 10 == num_one[0] + num_one[1]


@pytest.mark.regression
@pytest.mark.skipif(2 == 2, reason="2 == 2") # Пропускаем кейс, т. к. срабатывает условие 2 = 2.
def test_dz4():
    a = 1
    b = 2
    assert b / a == 2


@pytest.mark.functional
@pytest.mark.usefixtures('set_array_a', 'set_array_b')
@pytest.mark.xfail(reason="cause look at bug #1")
def test_dz5():
    a = 1
    b = 2
    c = 5
    assert a + b * c == 11
