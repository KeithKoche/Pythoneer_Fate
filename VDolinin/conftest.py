import pytest
import requests

@pytest.fixture(scope='function')
def say_started():
    print('TEST_START_RIGHT_NOW')
    return 7777

# def pytest_addoption(parser):
#     parser.addoption(
#         "--url",
#         default="https://httpbin.org",
#         help="This is req url"
#     )
#
#     parser.addoption(
#         "--method",
#         default="get",
#         choices=["get", "post", "put", "patch", "delete"],
#         help="Method to execute"
#     )


import pytest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="https://www.opencart.ru/")
    parser.addoption("--headless", action="store_true")



@pytest.fixture
def driver(request):
    _driver = None
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.headless = True
        _driver = webdriver.Chrome(
            executable_path=r"C:/Users/murse/PycharmProjects/pythonProject/drivers/chromedriver.exe", options=options)
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        if headless:
            options.headless = True
        _driver = webdriver.Firefox(
            executable_path=r"C:/Users/murse/PycharmProjects/pythonProject/drivers/geckodriver.exe",
            options=options)

    _driver.maximize_window()

    _driver.base_url = base_url
    catalog_url = "kompleksniy-resheniya/"
    _driver.catalog_url = base_url + catalog_url
    product_url = "torgovaya_ploshadka_opencart/"
    _driver.product_url = base_url + product_url
    login_url = "login/"
    _driver.login_url = base_url + login_url
    yield _driver

    _driver.quit()
