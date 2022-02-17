import math
import pytest



@pytest.mark.parametrize("x, y", [("a", "b")], indirect=["x"])
def test_indirect(x, y):
    assert x == "aaa"
    assert y == "b"

@pytest.mark.parametrize("test_input, expected_output",
                         [
                             (5, 25),
                             (9, 81),
                             (10, 100)
                         ]
                         )
def test_calc_square(test_input, expected_output):
    result = math.calc_square(test_input)
    assert result == expected_output

@pytest.mark.parametrize("d", [1, 3, 5])
@pytest.mark.parametrize("g", [2, 4, 6])
def test1234(d, g, f):
    assert d + g == 4