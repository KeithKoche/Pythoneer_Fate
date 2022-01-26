import pytest

"""тест"""
class Class_Test:
    def __init__(self, test_firsts_list5_test):
        self.test_firsts_list5_test = test_firsts_list5_test

    def __init__(self, test_firsts_list6_test):
        self.test_firsts_list6_test = test_firsts_list6_test


@pytest.fixture()
def test_firsts_list5_test():
    return 1


@pytest.fixture()
def test_firsts_list6_test():
    return 2


def test(Class_Test):
    assert Class_Test.test_firsts_list5_test == 1
    assert Class_Test.test_firsts_list6_test == 1
