import pytest
# from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from configparser import ConfigParser
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def setup(request):
    global url
    url = config_read()
    global driver
    opts = Options()
    opts.set_headless()
    assert opts.headless
    driver = Chrome(options=opts)
    driver.get(url['index'])
    yield driver
    driver.quit()


def config_read():
    config = ConfigParser()
    config.read('config.ini')
    index = config.get('url', 'index')
    account = config.get('url', 'account')
    acme = config.get('url', 'acme')
    return {'index': index, 'account': account, 'acme': acme}


@pytest.mark.usefixtures("setup")
def test_li():
    print(url['index'])
    # all = driver.find_elements_by_tag_name('li')
    all = driver.find_elements(By.TAG_NAME, 'li')
    for a in all:
        print(a.get_attribute('class'))
    assert all


@pytest.mark.usefixtures("setup")
def test_a():
    all = driver.find_elements_by_tag_name('a')
    for a in all:
        print(a.get_attribute('href'))
    assert all


@pytest.mark.usefixtures("setup")
def test_Privacy_Policy():
    Privacy_Policy = driver.find_element_by_link_text('Privacy Policy')
    print(Privacy_Policy.get_attribute('href'))
    assert Privacy_Policy


@pytest.mark.usefixtures("setup")
def test_twelve_eighty():
    all = driver.find_elements_by_xpath("//header/descendant::*")
    for i in all:
        print(i.get_attribute('id'))
    assert all


@pytest.mark.usefixtures("setup")
def test_US():
    # url = config_read()
    driver.get(url['account'])
    # driver.get('http://litecart.stqa.ru/index.php/en/create_account')
    select2 = driver.find_element_by_class_name('select2-container').click()
    select = driver.find_elements_by_class_name('select2-results__options')
    US = driver.find_element_by_xpath("//*[contains(text(), 'United States')]")
    print(US.get_attribute('innerHTML'))
    assert US


@pytest.mark.usefixtures("setup")
def test_US_zone():
    driver.get(url['account'])
    select2 = driver.find_element_by_class_name('select2-container').click()
    select = driver.find_elements_by_class_name('select2-results__options')
    US = driver.find_element_by_xpath("//*[contains(text(), 'United States')]").click()
    US_zone = driver.find_elements_by_xpath("//select[@name='zone_code']")
    for i in US_zone:
        print(i.text)
    assert US_zone


@pytest.mark.usefixtures("setup")
def test_US_zone_select():
    driver.get(url['account'])
    select2 = driver.find_element_by_class_name('select2-container').click()
    select = driver.find_elements_by_class_name('select2-results__options')
    US = driver.find_element_by_xpath("//*[contains(text(), 'United States')]").click()
    # US_zone = Select(driver.find_element_by_name('zone_code'))
    US_zone = Select(driver.find_element_by_xpath("//select[@name='zone_code']"))
    assert US_zone


@pytest.mark.usefixtures("setup")
def test_sort_date():
    driver.get(url['acme'])
    sort_date = driver.find_element_by_partial_link_text('Date')
    # sort_date = driver.find_element_by_xpath("//*[contains(text(), 'Date')]")
    print(sort_date.get_attribute('href'))
    assert sort_date


@pytest.mark.usefixtures("setup")
def test_zoomable():
    driver.get(url['acme'])
    zoomable = driver.find_element_by_class_name('fa')
    print(zoomable.get_attribute('class'))
    assert zoomable
