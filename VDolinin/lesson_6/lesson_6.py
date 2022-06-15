import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_first(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.base_url)
    wait.until(EC.visibility_of_element_located((By.ID, "button-demo")))
    assert "Opencart" in driver.title


def test_second(driver):
    driver.get(driver.base_url)
    driver.save_screenshot("example.png")


def test_elem(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.base_url)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login")))


def test_class(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.base_url)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "download-content-abs")))


def test_ohdfj(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.base_url)
    wait.until(EC.visibility_of_element_located((By.ID, "button-demo")))


def test_cat1(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.catalog_url)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "slider__item-img")))


def test_cat2(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.catalog_url)
    wait.until(EC.visibility_of_element_located((By.ID, "cart")))


def test_cat3(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.catalog_url)
    print(driver.window_handles)
    wait.until(EC.visibility_of_element_located((By.ID, "cart-total-img")))
    driver.find_element(by=By.ID, value="cart-total-img").click()
    wait.until(
        EC.visibility_of_element_located((By.NAME, "Корзина покупок")), message='Не дождался элемента')
    assert "Корзина покупок" in driver.title


def test_cat4(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.catalog_url)
    print(driver.window_handles)
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content\product>div:nth-child(2)>div>ul>li:nth-child(2)>a")),
        message='Не дождался элемента')
    driver.find_element(by=By.CSS_SELECTOR,
                        value="#content\product>div:nth-child(2)>div>ul>li:nth-child(2)>a").click()
    wait.until(EC.visibility_of_element_located((By.ID, "form-review")), message='Не дождался элемента')


def test_cat5(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.catalog_url)
    print(driver.window_handles)
    wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/aside/div[1]/a[2]")))
    driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/aside/div[1]/a[2]").click()
    assert "Шаблоны" in driver.title


def test_prod1(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.product_url)
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    driver.find_element(by=By.ID, value="button-cart").click()
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/form/div/div[1]/div")))


def test_prod2(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.product_url)
    wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#content\ product > div:nth-child(2) > div > ul > li:nth-child(2) > a")))


def test_prod3(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.product_url)
    wait.until(EC.visibility_of_element_located((By.NAME, "option[2031]")))
    driver.find_element(by=By.NAME, value="option[2031]").send_keys("license")
    wait.until(EC.visibility_of_element_located((By.ID, "button-cart")))
    driver.find_element(by=By.ID, value="button-cart").click()
    wait.until(EC.visibility_of_element_located((By.ID, "cart-total-img")))
    driver.find_element(by=By.ID, value="cart-total-img").click()
    wait.until(
        EC.visibility_of_element_located((By.XPATH, "/ html / body / div[2] / div / div / div / div / div[2] / a[2]")))


def test_prod4(driver):
    driver.get(driver.product_url)
    assert "Купить Cборка торговой площадки на Opencart" in driver.title


def test_prod5(driver):
    wait = WebDriverWait(driver, 5)
    driver.get(driver.product_url)
    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/a")))
    driver.find_element(by=By.XPATH,
                        value="/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/a").click()
    wait.until(EC.visibility_of_element_located((By.ID, "input-enquiry")), message='Не дождался элемента')


def test_login1(driver):  # при неправильном логине/пароле вылетает предупреждение.
    wait = WebDriverWait(driver, 5)
    driver.get(driver.login_url)
    wait.until(EC.visibility_of_element_located((By.NAME, "email")))
    wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    driver.find_element(by=By.NAME, value="email").send_keys("emptyuser")
    driver.find_element(by=By.NAME, value="password").send_keys("emptyuser")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#login>input.btn.btn-primary")))
    driver.find_element(by=By.CSS_SELECTOR, value="#login>input.btn.btn-primary").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")))


def test_login2(driver):  # Забыли пароль? Проверка почты с невалидными данными
    wait = WebDriverWait(driver, 5)
    driver.get(driver.login_url)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-right>div>a:nth-child(3)")))
    driver.find_element(by=By.CSS_SELECTOR, value="#column-right>div>a:nth-child(3)").click()
    wait.until(EC.visibility_of_element_located((By.ID, "forgotten__input-email")))
    driver.find_element(by=By.ID, value="forgotten__input-email").send_keys("bad_email")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content>form>div>div.pull-right>input")))
    driver.find_element(by=By.CSS_SELECTOR, value="#content>form>div>div.pull-right>input").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")))
