import json
import os
import re
from time import sleep, time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from constants import districts, type_org_mapping


# # Асинхронная функция для запроса через aiohttp
# async def fetch(session, url):
#     async with session.get(url) as response:
#         return await response.text()
#
#
# # Синхронная функция для запроса через Selenium
# def fetch_with_selenium(url):
#     driver = webdriver.Chrome()
#     driver.get(url)
#     content = driver.page_source
#     driver.close()
#     return content
#
#
# # Асинхронная функция для запуска синхронной функции в потоке
# async def fetch_with_selenium_async(url):
#     loop = asyncio.get_event_loop()
#     return await loop.run_in_executor(None, fetch_with_selenium, url)
#
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         html_content = await fetch(session, 'https://2gis.ru/moscow')
#         soup = BeautifulSoup(html_content, 'lxml')
#         # Добавьте код парсинга с использованием soup здесь
#
#         selenium_content = await fetch_with_selenium_async('https://2gis.ru/moscow')
#         # Обработайте содержимое selenium_content

def filter_links(hrefs):
    pattern = re.compile(r'^https://2gis\.ru/.+/firm/.+')
    return [href for href in hrefs if pattern.match(href)]


class CardSearcher:
    def __init__(self, driver, link='https://2gis.ru/moscow'):
        self.driver = driver
        self.slider = None
        self.link = link

    def page_parsing(self, city, district, type_org_ru, type_org):
        self.driver.get(self.link)
        # Запрос
        request = city + ' ' + district + ' ' + type_org_ru
        find_button = driver.find_element(By.CLASS_NAME, '_1gvu1zk')
        find_button.send_keys(request, Keys.ENTER)
        sleep(0.5)
        # включение сортировки по новизне
        find_sort = driver.find_element(By.CSS_SELECTOR, 'input._1e4yjns[type="text"][placeholder="Сортировка"]')
        find_sort.send_keys('По новизне', Keys.ENTER)

        sleep(0.3)
        # поиск количества точек
        find_places = driver.find_element(By.XPATH, '//div[@class="_nude0k3"]/a[@class="_rdxuhv3"]').text
        number_places = int(''.join(filter(str.isdigit, find_places)))
        print(f'Места: {number_places}')

        # поиск и сбор ссылок на компании
        find_cards = driver.find_element(By.CLASS_NAME, '_z72pvu')
        link_elements = find_cards.find_elements(By.CSS_SELECTOR, 'a')
        hrefs = [href.get_attribute('href') for href in link_elements]

        # чистка ссылок от рекламы
        hrefs = filter_links(hrefs)
        print(len(hrefs))

        directory = f'links/test/{type_org}'
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(f'links/test/{type_org}/{request}.json', 'w') as file:
            json.dump({'1': hrefs}, file)

        pass


if __name__ == '__main__':
    start_time = time()
    for type_org in ['sport']:
        i = 0
        # for district in districts:
        for district in ['Район сокол']:
            i += 1
            print(f"[INFO] Район: {i}/{len(districts)}")
            driver = webdriver.Chrome()
            grabber = CardSearcher(driver)
            grabber.page_parsing(city="Москва", district=district, type_org_ru=type_org_mapping[type_org],
                                 type_org=type_org)

    end_time = time()
    print(f'{(end_time - start_time):.1f} секунды на выполение')
    # asyncio.run(main())
