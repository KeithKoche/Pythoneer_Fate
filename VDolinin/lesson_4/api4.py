import pytest


@pytest.mark.parametrize("code", [200, 300, 400, 404, 500, 502])
# @pytest.fixture(scope="function", params={'zapros': 'null, sfhfhfhfhfhfhfhfh'})
def test_url_status(base_url, code, request_method):
    target = base_url + f"/"

    responce = request_method(url=target)

    assert responce.status_code == code
