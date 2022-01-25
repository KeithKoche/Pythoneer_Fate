import pytest

@pytest.fixture(scope='function')
def say_started():
    print('TEST_START_RIGHT_NOW')
    return 7777