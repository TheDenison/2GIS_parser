import asyncio
import re


from time import sleep
from urllib.parse import urljoin, urlparse

from constants import MY_HEADERS, LINK_NAMES, STATIONS, SITE_PATTERNS
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def process_link(base_url, link):
    parsed_link = urlparse(link)

    if parsed_link.scheme or parsed_link.netloc:  # Полная ссылка
        return link
    elif parsed_link.path.startswith('/'):  # Ссылка со слэшом в начале
        return urljoin(base_url, link)
    else:  # Дополняющая ссылка без слэша
        return urljoin(base_url, '/' + link)


class SoupContent(object):
    def get_name(self, soup_content):
        name = ''
        try:
            for data in soup_content.find_all("h1", {"class": "_tvxwjf"}):
                name = data.text
            return name
        except Exception:
            return ""

    def get_phone(self, soup_content):
        try:
            phones = []
            for data1 in soup_content.find_all('div', {"class": "_b0ke8"}):
                print(data1)
                for data in soup_content.find_all('a', {"class": "_2lcm958"}, href=True):
                    if data['href'].startswith('tel:'):
                        phones.append(data['href'].replace("tel:", ""))
            return '\n'.join(phones)
        except Exception:
            print('Не нашло телефоны')
            return ""

    def get_email(self, soup_content):
        email = ''
        try:
            for data in soup_content.find_all("div", {"class": "_49kxlr"}):
                temp = data.text
                if '@' in temp:
                    email = temp
                    break
            return email
        except Exception:
            return ""

    def get_address(self, soup_content):
        try:
            text = [outer.find('a', class_='_2lcm958').text for outer in soup_content.find_all('span', class_='_14quei') if outer.find('a', class_='_2lcm958')]
            text = ' '.join(text)
            text = text.replace("\u200B", "").replace(u"\xa0", u" ")
            address = text
            return address
        except Exception:
            return ""

    def get_website(self, soup_content):
        website = ''
        try:
            for a in soup_content.find_all('a', {'class': '_1rehek'}):
                link_text = a.text
                # Проверяем, не содержит ли текст ссылки http://, https:// или www.
                for s in SITE_PATTERNS:
                    if s in link_text:
                        website = link_text
                        break
            return website
        except Exception:
            return ""

    def get_rating(self, soup_content):
        rating = ""
        try:
            for data in soup_content.find_all("div", {"class": "_y10azs"}):
                rating += data.getText()
            return rating
        except Exception:
            return ""

    def get_reviews(self, soup_content):
        reviews = ""
        try:
            for data in soup_content.find_all("div", {"class": "_jspzdm"}):
                reviews += data.getText()
                # reviews = re.sub(r'Написать отзыв', '', reviews)
                # if reviews == "":
                #     reviews = soup_content.find("div", {"class": "business-header-rating-view__text"}).text
            return reviews
        except Exception:
            return ""

    def get_category(self, soup_content):
        category = ""
        try:
            data = soup_content.find('div', {'class': "_1idnaau"}).text
            category = data.replace("\u200B", "")
            return category
        except Exception:
            return ""

    def get_station(self, soup_content):
        station = ""
        temp = ""
        try:
            for data in soup_content.find_all("span", {"class": "_1w9o2igt"}):
                temp = data.text.replace("\u200B", "")

                for t in STATIONS:
                    # print(f'Станция {t} элемент {temp}')
                    if temp == t:
                        station = temp
                        break
            return station
        except Exception:
            print('Не нашло станцию')
            return ""

    def get_branch(self, soup_content):
        branch = ""
        pattern = re.compile(r"\d+ филиал(а|ов)?")
        try:
            for span in soup_content.find_all("span", {'class': '_er2xx9'}):
                for a in span.find_all('a', {'class': '_1rehek'}):
                    if pattern.search(a.text):
                        branch = a.text
                        break
            return branch
        except Exception:
            return ""

    def get_ip_inn(self, web_link):
        timeout = 5
        urls = {}
        # checked_url = []
        self.checked_url = []
        found_urls = [web_link]
        try:
            response = requests.get(web_link, headers=MY_HEADERS, timeout=timeout)
            # ee = response.status_code
            # print(ee)
            if response.status_code == 200:
                # Получаем содержимое страницы
                page_content = response.text

                # Создаем объект BeautifulSoup
                soup = BeautifulSoup(page_content, 'lxml')

                # Ищем ссылки по названиям и сохраняем URL
                for name in LINK_NAMES:
                    try:
                        link = soup.find('a', text=re.compile(name, re.IGNORECASE))
                        link = link['href']
                        if link:
                            url = process_link(web_link, link)
                            urls[name] = url
                            found_urls.append(url)
                        else:
                            urls[name] = ''
                    except Exception:
                        urls[name] = ''
        except Exception:
            print('Error connect')

        # Выводим URL
        # for name, url in urls.items():
        #     if url != '':
        #         print(name + " URL:", url)

        # Выводим найденные URL в виде списка
        print(f"({len(found_urls)}) Found URLs:", found_urls)
        try:
            ip = ''
            inn = ''
            str_half = ''
            str_full = ''
            for web_link in found_urls:
                # sleep(1)
                response = requests.get(web_link, headers=MY_HEADERS, timeout=timeout)
                if response.status_code == 200:
                    # print('OK!')
                    page_content = response.text
                    soup = BeautifulSoup(page_content, 'lxml')

                    ip_pattern = re.compile(
                        r'(ИП|Индивидуальный предприниматель)[ :]?(?:(?:[А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+ [А-ЯЁ][а-яё]+)|(?:[А-ЯЁ][а-яё]+ [А-ЯЁ]\.(?:\s[А-ЯЁ]\.|[А-ЯЁ]\.))|(?:[А-ЯЁ][а-яё]+))', )  # re.IGNORECASE

                    inn_pattern = re.compile(r'ИНН[:/]?[ ]?(\d{10,12})')

                    found_ip_elements = soup(text=ip_pattern)
                    found_inn_elements = soup(text=inn_pattern)

                    inn_element_td = soup.find('td', text=re.compile(r'ИНН\s*[:-]?\s*'))
                    inn_element_span = soup.find('span', text=re.compile(r'ИНН\s*[:-]?\s*'))

                    if found_ip_elements and ip == '':
                        for element in found_ip_elements:
                            match = re.search(ip_pattern, element)
                            if match:
                                ip_text = match.group()
                                ip = ip_text
                                # print(ip)
                            break

                    if found_inn_elements and inn == '':
                        for element in found_inn_elements:
                            match = re.search(inn_pattern, element)
                            if match:
                                inn_text = match.group(1)
                                inn = str("ИНН ") + str(inn_text)
                                # print(inn)
                            break

                    if inn_element_td and inn != '':
                        inn_number = inn_element_td.find_next_sibling('td').text
                        inn = str(inn_number).strip()
                    if inn_element_span and inn != '':
                        inn_number = inn_element_span.find_next_sibling('span').text
                        inn = str(inn_number).strip()

                    if ip != '' and inn == '':
                        str_half = f'{ip}'
                    if ip == '' and inn != '':
                        str_half = f'{inn}'
                    if ip and inn != '':
                        str_full = f'{ip} \n{inn}'
                        break
            if not str_full and str_half:
                return str_half

            if str_full:
                return str_full

        except requests.Timeout:
            print('Превышено время ожидания (тайм-аут)')
        except Exception:
            print("Не удалось получить доступ к странице")
