import pytest
@pytest.mark.parametrize("a, b, expected_result", [(10, 2, 5),
                                                   (15, 3, 5),
                                                   (20, 10, 2)])
def test_params_success(a, b, expected_result):
    assert a / b == expected_result

def test_simple_fixt(say_started):
    assert 1 == 1

def test_fixt_with_return(say_started):
    assert 1 == 1
    print(say_started)

@pytest.mark.usefixtures('say_started')
def test_with_mark():
    a = 3
    b = 5
    assert a * b == 15

@pytest.mark.skipif(1 == 1, reason="2 == 2")
def test_with_skip():
    a = 1
    b = 2
    assert a / b == 0.5