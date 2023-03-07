
# Запуск командой:
# python -m pytest -v --driver Chrome --driver-path web_driver/chromedriver.exe tests/test_negative_email.py

import pytest
from BasePages import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Тест EX-101 - проверка негативных сценариев в соответствие с ЧИТ-листом авторизации по почте
@pytest.mark.parametrize("email", ["   ", "Ф", "f", "DERJYTR", "горфтвку", "еНgTRe gtкУЦврuY ", "876 9876 0 ",
                                   "iA418uacJjxANioWlisogiY7nLqcmDH5tvNlCkUАдааушаЦГкущгуцквгуyfYBfNhhKbuuGwctkVrmWQT2qqkivUczHBq1BRLi2EnDbhsfohR4Z5lJlUAIk3n5f9p0hUhuzLbTDыафаругуГНВеЕРГГУГje45WLttvXjADSZWrP2XjgqAZOMV2A99eDnSIGw2z6NryXHPsOzxayKfc2JsF0Gi3KxFz4ON7qfZLkczXntrQqSFs8BW44hA8DRfccEB3IqQRHl",
                         ";?К;*((№));_№__;?№%&**(^%%@", "<script>alert(123)</script> ", "总全公事还原两么样", "♠♣♂◘♦☻"],
                         ids=["space", "Cyrillic letter", "Unicode letter", "Unicode letters", "Cyrillic letters",
                              "Combination of cyrillic and unicode letters", "int", "Long string", "SpecSimbols", "Injection", "Chinese symbols", "Combination of additional symbols"])
@pytest.mark.parametrize("passwd", ["   ", "Ф", "f", "DERJYTR", "горфтвку", "еНgTRe gtкУЦврuY ", "876 9876 0 ",
                                   "iA418uacJjxANioWlisogiY7nLqcmDH5tvNlCkUАдааушаЦГкущгуцквгуyfYBfNhhKbuuGwctkVrmWQT2qqkivUczHBq1BRLi2EnDbhsfohR4Z5lJlUAIk3n5f9p0hUhuzLbTDыафаругуГНВеЕРГГУГje45WLttvXjADSZWrP2XjgqAZOMV2A99eDnSIGw2z6NryXHPsOzxayKfc2JsF0Gi3KxFz4ON7qfZLkczXntrQqSFs8BW44hA8DRfccEB3IqQRHl",
                         ";?К;*((№));_№__;?№%&**(^%%@", "<script>alert(123)</script> ", "总全公事还原两么样", "♠♣♂◘♦☻"],
                         ids=["space", "Cyrillic letter", "Unicode letter", "Unicode letters", "Cyrillic letters",
                              "Combination of cyrillic and unicode letters", "int", "Long string", "SpecSimbols", "Injection", "Chinese symbols", "Combination of additional symbols"])
def test_101_negative_by_email_parametrized(browser, email, passwd):
    form = AuthForm(browser)

    # ввод почты
    form.username.send_keys(email)
    form.password.send_keys(passwd)
#    sleep(5)
    WebDriverWait(form.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "kc-login"))).click()
#    form.btn_click()

    err_mess = form.driver.find_element(By.ID, 'form-error-message')
    assert err_mess.text == 'Неверный логин или пароль'