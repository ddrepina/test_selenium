import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope="session")
def setup(request):
    global driver
    driver = webdriver.Chrome('D:\\programs\\chromedriver.exe')
    session = request.node
    # for item in session.items:
    #     cls = item.getparent(pytest.Class)
    #     setattr(cls.obj, "driver", driver)
    # time.sleep(9)
    driver.get('http://litecart.stqa.ru/index.php/en/')
    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
def test_li():
    all = driver.find_elements_by_tag_name('li')
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
    driver.get('http://litecart.stqa.ru/index.php/en/create_account')
    select2 = driver.find_element_by_class_name('select2-container').click()
    select = driver.find_elements_by_class_name('select2-results__options')
    US = driver.find_element_by_xpath("//*[contains(text(), 'United States')]")
    print(US.get_attribute('innerHTML'))
    assert US


@pytest.mark.usefixtures("setup")
def test_US_zone():
    driver.get('http://litecart.stqa.ru/index.php/en/create_account')
    select2 = driver.find_element_by_class_name('select2-container').click()
    select = driver.find_elements_by_class_name('select2-results__options')
    US = driver.find_element_by_xpath("//*[contains(text(), 'United States')]").click()
    US_zone = driver.find_elements_by_xpath("//select[@name='zone_code']")
    for i in US_zone:
        print(i.text)
    assert US_zone


@pytest.mark.usefixtures("setup")
def test_US_zone_select():
    driver.get('http://litecart.stqa.ru/index.php/en/create_account')
    select2 = driver.find_element_by_class_name('select2-container').click()
    select = driver.find_elements_by_class_name('select2-results__options')
    US = driver.find_element_by_xpath("//*[contains(text(), 'United States')]").click()
    # US_zone = Select(driver.find_element_by_name('zone_code'))
    US_zone = Select(driver.find_element_by_xpath("//select[@name='zone_code']"))
    assert US_zone


@pytest.mark.usefixtures("setup")
def test_sort_date():
    driver.get('http://litecart.stqa.ru/index.php/en/acme-corp-m-1/')
    sort_date = driver.find_element_by_partial_link_text('Date')
    # sort_date = driver.find_element_by_xpath("//*[contains(text(), 'Date')]")
    print(sort_date.get_attribute('href'))
    assert sort_date


@pytest.mark.usefixtures("setup")
def test_zoomable():
    driver.get('http://litecart.stqa.ru/index.php/en/acme-corp-m-1/')
    zoomable = driver.find_element_by_class_name('fa')
    print(zoomable.get_attribute('class'))
    assert zoomable
