from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config import read_config as config
import pytest


CHROMEDRIVER_PATH = './chromedriver.exe'
URL = 'http://litecart.stqa.ru/'


@pytest.fixture(scope='session')
def driver(request):
    opts = Options()
    # opts.add_argument("--headless")
    dr = webdriver.Chrome(CHROMEDRIVER_PATH, options=opts)
    # print(config.config_read()['sale'])
    dr.get(config.config_read()['sale'])

    yield dr

    def fin():
        dr.quit()

    request.addfinalizer(fin)
