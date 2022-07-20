from Pythoneer_Fate.VDolinin.lesson_7.classes.Opencart_classes import Opencart


def test_PO_cat5(driver): #проверка тайтла при переходе по заголовку
    Opencart(driver).open_catalog_page()
    Opencart(driver).template()
    Opencart(driver).check_title_template()

def test_PO_prod1(driver): #предупреждение о незаполненной лицензии
    Opencart(driver).open_product_page()
    Opencart(driver).buy_btn()
    Opencart(driver).check_alert_license()

def test_PO_prod3(driver): #проверка, что выбранный товар отображается в корзине
    Opencart(driver).open_product_page()
    Opencart(driver).input_license()
    Opencart(driver).buy_btn()
    Opencart(driver).cart_btn()
    Opencart(driver).check_product_in_cart()

def test_PO_prod4(driver): #проверить текст тайтла
    Opencart(driver).open_product_page()
    Opencart(driver).check_title()

def test_PO_login1(driver): # при неправильном логине и пароле вылетает предупреждение.
    Opencart(driver).open_login_page()
    Opencart(driver).input_email()
    Opencart(driver).input_password()
    Opencart(driver).login_btn()
    Opencart(driver).wait_wrong_warning()

def test_PO_login2(driver): #Забыли пароль? Вылетает предупреждение при вводе невалидного почтового ящика
    Opencart(driver).open_login_page()
    Opencart(driver).btn_forgot_pass()
    Opencart(driver).input_forgot_email()
    Opencart(driver).continue_btn()
    Opencart(driver).wait_warning()
