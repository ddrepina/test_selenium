
Десять правил построения хороших локаторов, мастер-класс
Во второй день конференции КоТэ (http://koteconf.ru/) Алексей Баранцев будет проводить мастер-класс по написанию "хороших" локаторов.
Чтобы как следует проникнуться этой темой, мы предлагаем вам заранее испробовать свои силы, выполнить серию заданий на построение локаторов. Используйте все свои знания и умения, старайтесь сделать локаторы как можно лучше! А на конференции Алексей проведёт разбор типовых ошибок, покажет те варианты, которые он считает "хорошими", и конечно расскажет обещанные десять правил.


<li class="product column shadow hover-light">
    <a class="link" href="http://litecart.stqa.ru/en/rubber-ducks-c-1/purple-duck-p-5" title="Purple Duck">
      <div class="image-wrapper">
        <img class="image" src="/cache/e9e885434e630e21e69b9e37fcab8e97cafb0058160x160_fwb.png" srcset="/cache/e9e885434e630e21e69b9e37fcab8e97cafb0058160x160_fwb.png 1x, /cache/e9e885434e630e21e69b9e37fcab8e97cafb0058320x320_fwb.png 2x" alt="Purple Duck">
              </div>
      <div class="name">Purple Duck</div>
      <div class="manufacturer">ACME Corp.</div>
      <div class="price-wrapper">
                <span class="price">$10</span>
              </div>
    </a>
        <a href="/images/products/5-purple-duck-1.png" class="fancybox zoomable" data-fancybox-group="product-listing" title="Purple Duck" style="position: absolute; top: 15px; right: 15px; color: inherit;" rel="product-listing"><i class="fa fa-search"></i></a>
    </li>

Все задания выполняются на сайте веб-магазина http://litecart.stqa.ru/index.php/en/

1. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ всех блоков (li) с информацией о товарах (каждому товару соответствует свой блок)
li = driver.find_element_by_tag_name('li')

2. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ всех ссылок (a) на страницы товаров в основной части страницы (не считая боковых блоков)
a = driver.find_element_by_tag_name('a')

3. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ ссылки на Privacy Policy в нижней части страницы
Privacy_Policy = driver.find_element_by_link_text('Privacy Policy')

4. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/ всех элементов верхнего меню, находящихся на верхнем уровне (без элементов вложенных выпадающих меню)
logotype-wrapper = driver.find_element_by_id('logotype-wrapper')
region-wrapper = driver.find_element_by_id('region-wrapper')
cart-wrapper = driver.find_element_by_id('cart-wrapper')

5. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/create_account элемента с текстом United States из выпадающего списка стран
select2-country_code-s4-result-6net-US = driver.find_element_by_id('select2-country_code-s4-result-6net-US')

6. На странице http://litecart.stqa.ru/index.php/en/create_account выберите страну United States и подберите локатор для выпадающего списка штатов
zone_code = driver.find_element_by_xpath("//select[@name='zone_code']")

7. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/acme-corp-m-1/ кнопки сортировки товаров по дате
sort_date = driver.find_element_by_xpath("xpath=//a[@href, 'http.*sort=date']")

8. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/acme-corp-m-1/ иконки-лупы для увеличения картинки товара, имеющего стикер Sale
fancybox_zoomable = driver.find_element_by_class_name("fancybox zoomable")

9. Подберите локатор для поиска на странице http://litecart.stqa.ru/index.php/en/acme-corp-m-1/ всех ссылок на товары, у которых нет стикера Sale


10. Добавьте в магазине http://litecart.stqa.ru/index.php/en/ в корзину 2-3 товара, перейдите на страницу оформления заказа http://litecart.stqa.ru/index.php/en/checkout и подберите локатор для поиска элемента, содержащего общую сумму к оплате
