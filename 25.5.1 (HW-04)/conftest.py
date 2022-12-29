import pytest
#import uuid
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')
    pytest.driver.implicitly_wait(30)
    pytest.driver.set_window_size(1400, 1000)

    yield

    pytest.driver.quit()

# @pytest.fixture(autouse=True)
# def testing():
#     pytest_driver = webdriver.Chrome('./chromedriver.exe')
#     # Переходим на страницу авторизации
#     pytest_driver.get('http://petfriends.skillfactory.ru/login')
#
#     yield
#
#     pytest_driver.quit()

# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     # This function helps to detect that some test failed
#     # and pass this information to teardown:
#
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# @pytest.fixture
# def web_browser(request, selenium):
#
#     browser = selenium
#     browser.set_window_size(1400, 1000)
#
#     # Return browser instance to test case:
#     yield browser
#
#     # Do teardown (this code will be executed after each test):
#
#     if request.node.rep_call.failed:
#         # Make the screen-shot if test failed:
#         try:
#             browser.execute_script("document.body.bgColor = 'white';")
#
#             # Make screen-shot for local debug:
#             browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')
#
#             # For happy debugging:
#             print('URL: ', browser.current_url)
#             print('Browser logs:')
#             for log in browser.get_log('browser'):
#                 print(log)
#
#         except:
#             pass  # just ignore any errors here


# firefox_options.binary — путь к exe-драйверу Firefox.
# firefox_options.add_argument(‘-foreground’) — возможность запуска в фоновом или реальном режиме.
#                              В нашем случае выбран последний. Для фонового укажите ‘-background’.
# firefox_options.set_preference(‘borwser.anchor_color’, ‘#FF0000’) — выбор цвета подложки браузера.
# @pytest.fixture
# def firefox_options(firefox_options):
#     firefox_options.binary = '/path/to/firefox-bin'
#     firefox_options.add_argument('-foreground')
#     firefox_options.set_preference('browser.anchor_color', '#FF0000')
#     return firefox_options
#
#
# # chrome_options.binary_location — путь к exe браузера (включая сам исполняемый файл).
# # chrome_options.add_extension — включение дополнений браузера.
# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.binary_location = '/path/to/chrome'
#     chrome_options.add_extension('/path/to/extension.crx')
#     chrome_options.add_argument('--kiosk')  # Также можно через эту конструкцию передать 100500 параметров браузера из списка
#     return chrome_options
#
# # Управление логированием
# @pytest.fixture
# def driver_args():
#     return ['--log-level=LEVEL']


# # Запуск браузера в режиме без UI
# @pytest.fixture
# def chrome_options(chrome_options):
#     chrome_options.set_headless(True)
#     return chrome_options
