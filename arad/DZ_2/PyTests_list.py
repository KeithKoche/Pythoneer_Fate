import pytest

"""тест"""
def test_dz1_test(self):
    a = 1
    b = 2
    assert a * b == 3


class Class_Test:

    def test_dz2_list1_test(self):
        a = [1, 2, 3]
        b = [3, 4, 5]
        assert a[-1] + b[-1] == 8

    def test_dz2_list2_test(self):
        a = [1, 2, 3]
        b = [3, 4, 5]
        assert a[2] == b[0]

    def test_dz2_list3_test(self):
        a = [1, 2, 3]
        b = [3, 4, 5]
        assert a != b

    def test_dz2_list4_test(self):
        a = [1, 2, 3]
        b = [3, 4, 5]
        assert a[2] == b[0]

    @pytest.mark.parametrize("test_dz2_list1_test, test_dz2_list2_test",
                             [([1, 2, 3], [1, 2, 3]), ([4, 2, 3], [4, 2, 3])])
    def test_firsts_list5_test(self, test_dz2_list1_test, test_dz2_list2_test):
        assert test_dz2_list1_test[0] - test_dz2_list2_test[0] == 0

    @pytest.mark.parametrize("test_dz2_list1_test, test_dz2_list2_test",
                             [([1, 2, 3], [1, 2, 3]), ([4, 2, 3], [4, 2, 3])])
    def test_firsts_list6_test(self, test_dz2_list1_test, test_dz2_list2_test):
        assert test_dz2_list1_test[0] - test_dz2_list2_test[0] == 0



