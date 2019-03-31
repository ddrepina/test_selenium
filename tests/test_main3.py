from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.ui import Select
import pytest
import time


URL = 'http://litecart.stqa.ru/index.php/en/'


@pytest.mark.skip
def test_li(driver):
    all = driver.find_elements_by_css_selector('li.product.column.shadow.hover-light')
    # all = driver.find_elements_by_css_selector('li.product')
    print(all)
    for a in enumerate(all):
        print(a[0], a[1].get_attribute('class'))


@pytest.mark.skip
def test_li2(driver):
    all = driver.find_elements_by_class_name('product')
    print(all)
    for a in enumerate(all):
        print(a[0], a[1].get_attribute('class'))


@pytest.mark.skip
def test_high_level1(driver):
    all = driver.find_elements_by_css_selector('li.product.column.shadow.hover-light')
    for a in all:
        target = a.find_element_by_class_name('link')
        if target.find_element_by_xpath('./*[@class="image-wrapper"]').text == '':
            goal = target.get_attribute('href')
            print(goal)


@pytest.mark.skip
def test_high_level1_exp(driver):
    all = driver.find_elements_by_css_selector('li.product.column.shadow.hover-light')
    for a in all:
        target = a.find_element_by_class_name('link')
        # if target.find_element_by_xpath('./div[@class="image-wrapper"][(not(descendant::div))]'):
        ff = target.find_elements_by_xpath('./a/*[not(child::div)]')
        for f in ff:
            print(f.get_attribute('class'), f.text)
        goal = target.get_attribute('href')
            # print(goal)


def test_high_level2(driver):
    all = driver.find_elements_by_css_selector('li.product.column.shadow.hover-light')
    for a in all:
        target = a.find_element_by_class_name('link')
        if target.find_element_by_xpath('./*[@class="image-wrapper"]').text == 'SALE':
            goal = target.get_attribute('href')
            print('HELLLLOOOOOOOOOOOOOO', goal)
            # driver.get(goal)
            # driver.save_screenshot('goal_{}.png'.format(datetime.now))
    driver.get(goal)
    driver.find_element_by_xpath('//*[@name="add_cart_product"]').click()
    s_size = Select(driver.find_element_by_xpath("//select[@name='options[Size]']"))
    s_size.select_by_visible_text('Small')
    driver.find_element_by_name('add_cart_product').click()
    time.sleep(2)
    driver.find_element_by_name('add_cart_product').click()
    time.sleep(2)
    driver.find_element_by_css_selector('a.image').click()
    time.sleep(1)
    # td = driver.find_element_by_xpath('//tr[@class="footer"]/td[last()]')
    td = driver.find_element_by_xpath('//tr[@class="footer"]/td[not(@colspan)]')
    print(td.text)
