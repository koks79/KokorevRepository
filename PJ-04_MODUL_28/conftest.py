import pytest
from selenium import webdriver


@pytest.fixture
def browser(chrome_options):
    driver = webdriver.Chrome(executable_path="./web_driver/chromedriver")
    chrome_options.add_argument('--incognito')
    yield driver
    driver.quit()
