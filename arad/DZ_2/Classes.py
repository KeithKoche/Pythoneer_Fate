import pytest

"""тест"""
@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


def test_eval():
    a = list(range(1, 5, 1))
    print(a)
    assert eval(test_input) == expected
