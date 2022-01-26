import pytest

"""тест"""
class Class_Test:

    def test_dz2_Set1_test(self):
        a = {1, 2, 3}
        assert 1 in a

    def test_dz2_Set2_test(self):
        a = {1, 2}
        a.add(3)
        assert 3 in a

    def test_dz2_Set3_test(self):
        a = {1, 2, 3}
        a.discard(3)
        assert 3 not in a

    def test_dz2_Set4_test(self):
        a = {1, 2}
        b = {2, 3}
        c = a.union(b)
        assert c == {1, 2, 3}

    @pytest.mark.parametrize("test_dz2_set1, test_dz2_set2", [(({1, 2}), ({2, 3})), (({3, 2}), ({2, 4}))])
    def test_firsts_set5_test(self, test_dz2_set1, test_dz2_set2):
        assert test_dz2_set1 & test_dz2_set2 == {2}