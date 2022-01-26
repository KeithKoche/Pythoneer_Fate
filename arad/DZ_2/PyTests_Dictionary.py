import pytest

"""тест"""
class Class_Test:

    def test_dz2_Dict1_test(self):
        a = {1: 1, 2: 2, 3: 3}
        assert a[1] == 1

    def test_dz2_Dict2_test(self):
        a = {1: "one", 2: "two"}
        a[1] = "four"
        assert a[1] == "four"

    def test_dz2_Dict3_test(self):
        a = {1: "one", 2: "two"}
        a[3] = "four"
        assert len(a) == 3

    def test_dz2_Dict4_test(self):
        a = {"one": 1, 2: "two"}
        b = {"four": 4}
        assert a["one"] + b["four"] == 5

    @pytest.mark.parametrize("a, b, c", [(1, 2, 3), (3, 2, 1)])
    def test_firsts_dict5_test(self, a, b, c):
        dict_a = {1: a}
        dict_b = {1: b}
        dict_c = {1: c}
        assert dict_a[1] + dict_b[1] + dict_c[1] == 6
