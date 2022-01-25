import pytest
from datetime import datetime


@pytest.fixture(scope="session", autouse=True)
def set_time():
    start_date = datetime.now()
    yield
    last_date = datetime.now()
    print("\n", last_date - start_date)


def array(n):
    arr = [i for i in range(n)]
    return arr


@pytest.fixture(params=(range(10)))
def set_array_a(request):
    arr1 = array(10)
    return request.param


@pytest.fixture(params=(range(10)))
def set_array_b(request):
    return request.param


@pytest.fixture(scope='function', params=(range(1, 6)))
def num_one(request, num_two):
    return request.param, num_two


@pytest.fixture(scope='function', params=(range(10, 60, 10)))
def num_two(request):
    return request.param
