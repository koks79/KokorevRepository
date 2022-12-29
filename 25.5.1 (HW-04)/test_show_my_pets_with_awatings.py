# Команда для выполнения
# python -m pytest -v -rA --driver Chrome --driver-path chromedriver.exe test_show_my_pet_with_awaitings.py
# из папки C:\Users\Admin\PycharmProjects\pythonSelenium_24modul\tests>

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

email = 'koks79@list.ru'
passwd = '12345'


def test_all_of_pets_are_present():
    # Вводим email
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
#    pytest.driver.find_element(By.ID, "email").send_keys(email)
    # Вводим пароль
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(passwd)
#    pytest.driver.find_element(By.ID, "pass").send_keys(passwd)
#    time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
#    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
#    time.sleep(3)
    # Нажимаем на кнопку "Мои питомцы"
    WebDriverWait(pytest.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a'))).click()
#    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
#    time.sleep(3)
    # Проверяем, что мы оказались на главной странице пользователя
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h2'))).text != ""
#    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text != ""

#    images = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets>table>tbody>tr>th>img')
#    all_pets = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')))
    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    # descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')
    pets_numb = int(WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class=".col-sm-4 left"]'))).text.split('\n')[1].split(":")[1])
#    pets_numb = int(pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1])

    print('Количество питомцев по статистике пользователя:', pets_numb)
    print('Количество питомце по количеству строк в таблице:', len(all_pets))

    assert pets_numb == len(all_pets)


def test_foto_of_pets():
    # Вводим email
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    #    pytest.driver.find_element(By.ID, "email").send_keys(email)
    # Вводим пароль
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(passwd)
    #    pytest.driver.find_element(By.ID, "pass").send_keys(passwd)
    #    time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    #    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    #    time.sleep(3)
    # Нажимаем на кнопку "Мои питомцы"
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a'))).click()
    #    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    #    time.sleep(3)
    # Проверяем, что мы оказались на главной странице пользователя
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h2'))).text != ""
    #    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text != ""

    images = pytest.driver.find_elements(By.CSS_SELECTOR, 'div#all_my_pets>table>tbody>tr>th>img')
    # names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    # descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    pets_numb = int(pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1])

    print('Количество питомцев:', pets_numb)
    print(type(pets_numb))

    count = 0
    for i in range(pets_numb-1):
        if images[i].get_attribute('src') != '':
            count = count + 1

    assert count > pets_numb // 2


def test_same_names_of_pets():
    # Вводим email
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    #    pytest.driver.find_element(By.ID, "email").send_keys(email)
    # Вводим пароль
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(passwd)
    #    pytest.driver.find_element(By.ID, "pass").send_keys(passwd)
    #    time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    #    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    #    time.sleep(3)
    # Нажимаем на кнопку "Мои питомцы"
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a'))).click()
    #    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    #    time.sleep(3)
    # Проверяем, что мы оказались на главной странице пользователя
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h2'))).text != ""
    #    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text != ""

    pets_numb = int(pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1])
    print('Количество питомцев:', pets_numb)

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    print(len(all_pets))

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pet_names = []
    for pet in all_pets:
        pet_names.append(pet.text.split(' ')[0])
    print(pet_names)

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pets_data = [pet.text for pet in all_pets]
    not_uniq_pets = set([pet.text for pet in all_pets if pets_data.count(pet.text) > 1])
    print(f'Питомцы с повторяющимся именем {not_uniq_pets}')

    assert not_uniq_pets


def test_name_type_age_of_pet():
    # Вводим email
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    #    pytest.driver.find_element(By.ID, "email").send_keys(email)
    # Вводим пароль
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(passwd)
    #    pytest.driver.find_element(By.ID, "pass").send_keys(passwd)
    #    time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    #    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    #    time.sleep(3)
    # Нажимаем на кнопку "Мои питомцы"
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a'))).click()
    #    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    #    time.sleep(3)
    # Проверяем, что мы оказались на главной странице пользователя
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h2'))).text != ""
    #    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text != ""

    pets_numb = int(
        pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1])
    print('Количество питомцев:', pets_numb)

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    print(len(all_pets))

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pet_names = []
    pet_types = []
    for pet in all_pets:
        text = pet.text.replace("\n", " ").split()
        print(text)
        pet_names.append(text[0])
        assert len(text) == 4
#        pet_types.append(text[1])
#        print(pet_names)
#        pet_types.append(pet.text.split(' ')[1])
    print(pet_names)
    print(pet_types)

def test_same_pets():
    # Вводим email
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email"))).send_keys(email)
    #    pytest.driver.find_element(By.ID, "email").send_keys(email)
    # Вводим пароль
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(passwd)
    #    pytest.driver.find_element(By.ID, "pass").send_keys(passwd)
    #    time.sleep(2)
    # Нажимаем на кнопку входа в аккаунт
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))).click()
    #    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    #    time.sleep(3)
    # Нажимаем на кнопку "Мои питомцы"
    WebDriverWait(pytest.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a'))).click()
    #    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    #    time.sleep(3)
    # Проверяем, что мы оказались на главной странице пользователя
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h2'))).text != ""
    #    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text != ""

    pets_numb = int(
        pytest.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1])
    print('Количество питомцев:', pets_numb)

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    print(len(all_pets))

    all_pets = pytest.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
    pets_data = [pet.text for pet in all_pets]
    uniq_pets = set(pets_data)
    assert len(pets_data) == len(uniq_pets)
