from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Opencart:

    def __init__(self, driver):
        self.driver = driver

    def open_login_page(self):  # открыть ссылку логина
        self.driver.get("https://www.opencart.ru/login/")

    def open_product_page(self): #открыть страницу продукта
        self.driver.get("https://www.opencart.ru/torgovaya_ploshadka_opencart/")

    def open_catalog_page(self): #открыть страницу каталога
        self.driver.get("https://www.opencart.ru/kompleksniy-resheniya/")

    def invalid_email(self):  # ввод невалидного е-мейла login2
        wait = WebDriverWait(self, 5)
        self.driver.find_element(By.LINK_TEXT, "Забыли пароль?").click()
        self.driver.find_element(by=By.ID, value="forgotten__input-email").clear()
        self.driver.find_element(by=By.ID, value="forgotten__input-email").send_keys("email")
        self.driver.find_element(by=By.CSS_SELECTOR, value="div.pull-right>input").click()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")))

    def btn_forgot_pass(self, time=5): # login2
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.FORGOT_PASSWORD_BTN)))
        self.driver.find_element(By.LINK_TEXT, "Забыли пароль?").click()

    def input_forgot_email(self, time=5): #login2
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.INPUT_FORGOT_EMAIL)))
        self.driver.find_element(by=By.ID, value="forgotten__input-email").clear()
        self.driver.find_element(by=By.ID, value="forgotten__input-email").send_keys("email")

    def continue_btn(self, time=5): #login2
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.pull-right>input")))
        self.driver.find_element(by=By.CSS_SELECTOR, value="div.pull-right>input").click()

    def wait_warning(self, time=5): #login2
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.WARNING)))

    def input_email(self, time=5): #login1
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.INPUT_EMAIL)))
        self.driver.find_element(by=By.NAME, value="email").clear()
        self.driver.find_element(by=By.NAME, value="email").send_keys("email")

    def input_password(self, time=5): #login1
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.INPUT_PASSWORD)))
        self.driver.find_element(by=By.NAME, value="password").clear()
        self.driver.find_element(by=By.NAME, value="password").send_keys("password")

    def login_btn(self, time=5): #login1
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.ENTER_BTN)))
        self.driver.find_element(by=By.CSS_SELECTOR, value="#login>input.btn.btn-primary").click()

    def wait_wrong_warning(self, time=5): #login1
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.WRONG_WARNING)))

    def check_title(self): #prod4
        assert "Купить Cборка торговой площадки на Opencart" in self.driver.title

    def input_license(self, time=5): #prod3
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.INPUT_LICENSE)))
        self.driver.find_element(by=By.ID, value="input-option2031").clear()
        self.driver.find_element(by=By.ID, value="input-option2031").send_keys("license")

    def buy_btn(self, time=5): #prod3, prod1
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.BUY_BTN)))
        self.driver.find_element(by=By.ID, value="button-cart").click()

    def cart_btn(self, time=5): #prod3
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.CART_BTN)))
        self.driver.find_element(by=By.ID, value="cart-total-img").click()

    def check_product_in_cart(self, time=5): #prod3
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.PRODUCT_NAME)))

    def check_alert_license(self, time=5): #prod3
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.ALERT_LICENSE)))

    def template(self, time=5): #cat5
        WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((WaitLocators.TEMPLATE_BTN)))
        self.driver.find_element(by=By.LINK_TEXT, value="Шаблоны").click()

    def check_title_template(self, time=5): #cat5
        assert "Шаблоны" in self.driver.title


class WaitLocators():
    WARNING = (By.TAG_NAME, "DIV")
    FORGOT_PASSWORD_BTN = (By.LINK_TEXT, "Забыли пароль?")
    INPUT_FORGOT_EMAIL = (By.ID, "forgotten__input-email")
    CONTINUE_BTN = (By.CSS_SELECTOR, "div.pull-right>input")
    INPUT_EMAIL = (By.NAME, "email")
    INPUT_PASSWORD = (By.NAME, "password")
    ENTER_BTN = (By.CSS_SELECTOR, "#login>input.btn.btn-primary")
    WRONG_WARNING = (By.CSS_SELECTOR, "div.alert.alert-danger.alert-dismissible")
    INPUT_LICENSE = (By.ID, "input-option2031")
    BUY_BTN = (By.ID, "button-cart")
    CART_BTN = (By.ID, "cart-total-img")
    PRODUCT_NAME = (By.LINK_TEXT, "Cборка торговой площадки на Opencart")
    ALERT_LICENSE = (By.CSS_SELECTOR, "#product>div.options__line.form-group.required.has-error>div")
    TEMPLATE_BTN = (By.LINK_TEXT, "Шаблоны")
