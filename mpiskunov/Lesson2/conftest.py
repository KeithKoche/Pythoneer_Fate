import pytest
from datetime import datetime


@pytest.fixture(scope='session')
def set_time():
    start_date = datetime.now()
    yield
    last_date = datetime.now()
    print(start_date - last_date)

@pytest.fixture(params=(1,2,3,4,5))
def numb(request):
    return request.param