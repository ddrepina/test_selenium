import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


@pytest.fixture(scope="session")
def setup(request):
    driver = webdriver.Chrome('D:\\programs\\chromedriver.exe')
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    # time.sleep(9)
    driver.get('http://litecart.stqa.ru/index.php/en/')

    yield driver
    driver.close()


@pytest.mark.usefixtures("setup")
class TestExampleOne:
    def test_li(self):
        all = self.driver.find_elements_by_tag_name('li')
        for a in all:
            print(a.get_attribute('class'))
        assert all


    def test_a(self):
        all = self.driver.find_elements_by_tag_name('a')
        for a in all:
            print(a.get_attribute('href'))
        assert all


    def test_Privacy_Policy(self):
        Privacy_Policy = self.driver.find_element_by_link_text('Privacy Policy')
        print(Privacy_Policy.get_attribute('href'))
        assert Privacy_Policy


    def test_twelve_eighty(self):
        all = self.driver.find_elements_by_xpath("//header/descendant::*")
        for i in all:
            print(i.get_attribute('id'))
        assert all


    def test_US(self):
        self.driver.get('http://litecart.stqa.ru/index.php/en/create_account')
        select2 = self.driver.find_element_by_class_name('select2-container').click()
        select = self.driver.find_elements_by_class_name('select2-results__options')
        US = self.driver.find_element_by_xpath("//*[contains(text(), 'United States')]")
        print(US.get_attribute('innerHTML'))
        assert US


    def test_US_zone(self):
        self.driver.get('http://litecart.stqa.ru/index.php/en/create_account')
        select2 = self.driver.find_element_by_class_name('select2-container').click()
        select = self.driver.find_elements_by_class_name('select2-results__options')
        US = self.driver.find_element_by_xpath("//*[contains(text(), 'United States')]").click()
        US_zone = self.driver.find_elements_by_xpath("//select[@name='zone_code']")
        for i in US_zone:
            print(i.text)
        assert US_zone


    def test_US_zone_select(self):
        self.driver.get('http://litecart.stqa.ru/index.php/en/create_account')
        select2 = self.driver.find_element_by_class_name('select2-container').click()
        select = self.driver.find_elements_by_class_name('select2-results__options')
        US = self.driver.find_element_by_xpath("//*[contains(text(), 'United States')]").click()
        # US_zone = Select(self.driver.find_element_by_name('zone_code'))
        US_zone = Select(self.driver.find_element_by_xpath("//select[@name='zone_code']"))
        assert US_zone


    def test_sort_date(self):
        self.driver.get('http://litecart.stqa.ru/index.php/en/acme-corp-m-1/')
        sort_date = self.driver.find_element_by_partial_link_text('Date')
        # sort_date = self.driver.find_element_by_xpath("//*[contains(text(), 'Date')]")
        print(sort_date.get_attribute('href'))
        assert sort_date


    def test_zoomable(self):
        self.driver.get('http://litecart.stqa.ru/index.php/en/acme-corp-m-1/')
        zoomable = self.driver.find_element_by_class_name('fa')
        print(zoomable.get_attribute('class'))
        assert zoomable
