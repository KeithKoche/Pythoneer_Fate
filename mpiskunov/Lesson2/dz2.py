import pytest
import datetime

@pytest.mark.xfail(reason="fail")
def test_one_fail():
    a = 3
    b = 6
    assert a + b == 10

@pytest.mark.xfail(reason="fail")
@pytest.mark.usefixtures('set_time')
def test_two_fixt():
    b = str("abc")
    c = str("abd")
    assert b == c

@pytest.mark.skip()
@pytest.mark.smoke
def test_three():
    my_date = datetime.date(2022, 1, 10)
    i_date = datetime.date(2022, 1,25)
    first_date = datetime.date(my_date)
    second_date = datetime.date(i_date)
    delta = second_date - first_date
    print(delta)


@pytest.mark.regress
@pytest.mark.parametrize(("one, two"), [(1,2), (1,3), (1,4), (1,5)])
def test_four(one, two, numb):
    assert one + two == numb

@pytest.mark.regress
@pytest.mark.parametrize(("one, two"), [(2,4), (3,3), (3,5), (4,5)])
def test_five (one, two):
    assert one * two == 20