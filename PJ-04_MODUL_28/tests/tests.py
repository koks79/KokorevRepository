from time import sleep
from BasePages import *
from settings import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск командой:
# python -m pytest -v --driver Chrome --driver-path web_driver/chromedriver.exe tests/tests.py


# Тест EX-02 - общий вид формы (сохранить скриншот)
def test_02_screenshot(browser):
    form = AuthForm(browser)
    form.driver.save_screenshot('screenshot_001.jpg')


# Тест EX-05 - проверка, что по-умолчанию выбрана форма авторизации по телефону
def test_05_by_phone_default(browser):
    form = AuthForm(browser)

    assert form.placeholder.text == 'Мобильный телефон'


# Тест EX-06 - проверка автосмены "таб ввода"
def test_06_auto_change_placeholder(browser):
    form = AuthForm(browser)

    # ввод телефона
    form.username.send_keys('+79999999999')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Мобильный телефон'

    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод почты
    form.username.send_keys('test@test.ru')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Электронная почта'

    # очистка поля логина
    form.username.send_keys(Keys.CONTROL, 'a')
    form.username.send_keys(Keys.DELETE)

    # ввод логина
    form.username.send_keys('MyLogin')
    form.password.send_keys('_')
    sleep(5)

    assert form.placeholder.text == 'Логин'


# Тест EX-07 - проверка позитивного сценария авторизации по телефону
def test_07_positive_by_phone(browser):
    form = AuthForm(browser)

    # ввод телефона
    form.username.send_keys(valid_phone)
    form.password.send_keys(valid_pass)
    WebDriverWait(form.driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-login"))).click()
    # sleep(5)
    # form.btn_click()

    assert form.get_current_url() == '/account_b2c/page'


# Тест EX-08 - проверка негативного сценария авторизации по телефону
def test_08_negative_by_phone(browser):
    form = AuthForm(browser)

    # ввод телефона
    form.username.send_keys('+79999999999')
    form.password.send_keys('any_password')
    WebDriverWait(form.driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-login"))).click()
    # sleep(5)
    # form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'


# Тест EX-09 - проверка позитивного сценария авторизации по почте
def test_09_positive_by_email(browser):
    form = AuthForm(browser)

    # ввод почты
    form.username.send_keys(valid_email)
    form.password.send_keys(valid_pass)
    WebDriverWait(form.driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-login"))).click()
    # sleep(5)
    # form.btn_click()

    assert form.get_current_url() == '/account_b2c/page'


# Тест EX-10 - проверка негативного сценария авторизации по почте
def test_10_negative_by_email(browser):
    form = AuthForm(browser)

    # ввод почты
    form.username.send_keys('test@test.ru')
    form.password.send_keys('any_password')
    WebDriverWait(form.driver, 10).until(EC.element_to_be_clickable((By.ID, "kc-login"))).click()
    # sleep(5)
    # form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'


# # Тест EX-101 - проверка негативных сценариев в соответствие с ЧИТ-листом авторизации по почте
# @pytest.mark.parametrize("email", ["   ", "Ф", "f", "DERJYTR", "горфтвку", "еНgTRe gtкУЦврuY ", "876 9876 0 ",
#                                    "iA418uacJjxANioWlisogiY7nLqcmDH5tvNlCkUАдааушаЦГкущгуцквгуyfYBfNhhKbuuGwctkVrmWQT2qqkivUczHBq1BRLi2EnDbhsfohR4Z5lJlUAIk3n5f9p0hUhuzLbTDыафаругуГНВеЕРГГУГje45WLttvXjADSZWrP2XjgqAZOMV2A99eDnSIGw2z6NryXHPsOzxayKfc2JsF0Gi3KxFz4ON7qfZLkczXntrQqSFs8BW44hA8DRfccEB3IqQRHl",
#                          ";?К;*((№));_№__;?№%&**(^%%@", "<script>alert(123)</script> ", "总全公事还原两么样", "♠♣♂◘♦☻"],
#                          ids=["space", "Cyrillic letter", "Unicode letter", "Unicode letters", "Cyrillic letters",
#                               "Combination of cyrillic and unicode letters", "int", "Long string", "SpecSimbols", "Injection", "Chinese symbols", "Combination of additional symbols"])
# @pytest.mark.parametrize("passwd", ["   ", "Ф", "f", "DERJYTR", "горфтвку", "еНgTRe gtкУЦврuY ", "876 9876 0 ",
#                                    "iA418uacJjxANioWlisogiY7nLqcmDH5tvNlCkUАдааушаЦГкущгуцквгуyfYBfNhhKbuuGwctkVrmWQT2qqkivUczHBq1BRLi2EnDbhsfohR4Z5lJlUAIk3n5f9p0hUhuzLbTDыафаругуГНВеЕРГГУГje45WLttvXjADSZWrP2XjgqAZOMV2A99eDnSIGw2z6NryXHPsOzxayKfc2JsF0Gi3KxFz4ON7qfZLkczXntrQqSFs8BW44hA8DRfccEB3IqQRHl",
#                          ";?К;*((№));_№__;?№%&**(^%%@", "<script>alert(123)</script> ", "总全公事还原两么样", "♠♣♂◘♦☻"],
#                          ids=["space", "Cyrillic letter", "Unicode letter", "Unicode letters", "Cyrillic letters",
#                               "Combination of cyrillic and unicode letters", "int", "Long string", "SpecSimbols", "Injection", "Chinese symbols", "Combination of additional symbols"])
# def test_101_negative_by_email_parametrized(browser, email, passwd):
#     form = AuthForm(browser)
#
#     # ввод почты
#     form.username.send_keys(email)
#     form.password.send_keys(passwd)
#     sleep(5)
#     form.btn_click()
#
#     err_mess = form.driver.find_element(By.ID, 'form-error-message')
#     assert err_mess.text == 'Неверный логин или пароль'


# Тест EX-16 - проверка получения временного кода на телефон и открытия формы для ввода кода
def test_16_get_code_on_phone(browser):
    form = CodeForm(browser)

    # ввод телефона
    form.address.send_keys(valid_phone)

    # длительная пауза предназначена для ручного ввода капчи при необходимости
    sleep(50)
    form.get_click()

    rt_code = form.driver.find_element(By.ID, 'rt-code-0')

    assert rt_code


# Тест EX-20 - проверка перехода в форму восстановления пароля и её открытия
def test_20_forgot_pass_restore(browser):
    form = AuthForm(browser)

    # клик по надписи "Забыл пароль"
    form.forgot.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Восстановление пароля'


# Тест EX-21 - проверка перехода в форму регистрации и её открытия
def test_21_get_registration_form(browser):
    form = AuthForm(browser)

    # клик по надписи "Зарегистрироваться"
    form.register.click()
    sleep(5)

    reset_pass = form.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Регистрация'


# Тест EX-22 - проверка открытия пользовательского соглашения
def test_22_get_agreement_form(browser):
    form = AuthForm(browser)

    original_window = form.driver.current_window_handle
    # клик по надписи "Пользовательским соглашением" в подвале страницы
    form.agree.click()
    sleep(5)
    WebDriverWait(form.driver, 5).until(EC.number_of_windows_to_be(2))
    for window_handle in form.driver.window_handles:
        if window_handle != original_window:
            form.driver.switch_to.window(window_handle)
            break
    win_title = form.driver.execute_script("return window.document.title")

    assert win_title == 'User agreement'


# Тест EX-23 - проверка перехода по ссылке авторизации пользователя через вконтакте
def test_23_get_auth_vk_form(browser):
    form = AuthForm(browser)
    form.vk_btn.click()
    sleep(5)

    assert form.get_base_url() == 'oauth.vk.com'


# Тест EX-24 - проверка перехода по ссылке авторизации пользователя через одноклассники
def test_24_get_auth_ok_form(browser):
    form = AuthForm(browser)
    form.ok_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.ok.ru'


# Тест EX-25 - проверка перехода по ссылке авторизации пользователя через майлру
def test_25_get_auth_mailru_form(browser):
    form = AuthForm(browser)
    form.mailru_btn.click()
    sleep(5)

    assert form.get_base_url() == 'connect.mail.ru'


# Тест EX-26 - проверка перехода по ссылке авторизации пользователя через google
def test_26_get_auth_google_form(browser):
    form = AuthForm(browser)
    form.google_btn.click()
    sleep(5)

    assert form.get_base_url() == 'accounts.google.com'


# Тест EX-27 - проверка перехода по ссылке авторизации пользователя через яндекс
def test_27_get_uth_ya_form(browser):
    form = AuthForm(browser)
    form.ya_btn.click()
    sleep(5)

    assert form.get_base_url() == 'passport.yandex.ru'
