import csv
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from queue import Queue
from typing import Any

from requests import Session
from requests import RequestException
from selectolax.parser import HTMLParser

from rozetka_db import Product, Price, Image


class RozetkaListingParser:
    TIMEOUT = 10
    field_names = (
        'title', 'monitor', 'cpu', 'memory', 'drive',
        'old_price', 'new_price', 'discount', 'images'
    )
    LOCK = threading.Lock()

    def __init__(self, main_url: str, last_page: int):
        self._main_url = main_url
        self._last_page = last_page
        self.session = Session()
        self._id_counter = 0

    def scrape(self):
        que = self._fill_queue()
        print('Starting scraping...')
        with open('files/notebooks.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.field_names)
            writer.writeheader()

        with ThreadPoolExecutor(max_workers=99) as executor:
            for i in range(self._last_page):
                executor.submit(self._scrape, que)

        print('Finished scrapper')

    def _fill_queue(self):
        que = Queue()
        for page in range(1, self._last_page + 1):
            que.put(f'{self._main_url}page={page}/')
        return que

    def _scrape(self, que: Queue):
        while que.qsize():
            url = que.get()
            print(que.qsize(), url)
            try:
                response_text = self._get_response(url)  # Waiting
                self._parse(response_text)
            except Exception as error:
                print('Error', error)
                que.put(url)

    def _get_response(self, url: str) -> str | None:
        try:
            response = self.session.get(url, timeout=self.TIMEOUT)
            return response.text
        except RequestException as error:
            print('Request error', error)

    def _parse(self, html_string: str) -> None:
        tree = HTMLParser(html_string)
        result_list = []
        items = [item for item in tree.css('.item')]
        with self.LOCK:
            for item in items:
                title = item.css('.tile-title')
                if not title:
                    continue
                self._id_counter += 1
                information = title[0].text().split('/')
                old_price = item.css('.old-price')
                new_price = item.css('.price')
                images = item.css('.tile-image')
                image_links = [link.attrs.get('src') for link in images if
                               link.attrs.get('src')]
                item = {
                    'id': self._id_counter,
                    'title': information[0].strip(),
                    'monitor': information[1].strip() if len(
                        information) > 1 else '',
                    'cpu': information[2].strip() if len(information) > 2 else '',
                    'memory': information[3].strip() if len(
                        information) > 3 else '',
                    'drive': information[4].strip() if len(information) > 4 else '',
                    'old_price': (old := int(''.join(
                        [symbol for symbol in old_price[0].text() if
                         symbol.isdigit()])) if old_price else ''),
                    'new_price': (new := int(''.join(
                        [symbol for symbol in new_price[0].text() if
                         symbol.isdigit()])) if new_price else ''),
                    'discount': round(
                        (old - new) / old * 100) if old and new else 0,
                    'images': image_links if image_links else [],
                }
                result_list.append(item)
                # TODO Переписати запис у бачу всім списком а не окремо `bulk_create` or `insert_many`

            prices = [
                Price(
                    id=item.get('id'),
                    price=item.get('new_price'),
                    old_price=item.get('old_price', None),
                    discount=item.get('discount', 0)
                )
                for item in result_list
            ]
            Price.bulk_create(prices, batch_size=1000)
            products = [
                Product(
                    id=item.get('id'),
                    title=item.get('title'),
                    monitor=item.get('monitor'),
                    cpu=item.get('cpu'),
                    memory=item.get('memory'),
                    drive=item.get('drive'),
                    price_id=prices[i].id
                )
                for i, item in enumerate(result_list)
            ]
            Product.bulk_create(products)
            images = [
                Image(
                    product_id=products[i].id,
                    url_link=image_link
                )
                for i, item in enumerate(result_list)
                for image_link in item.get('images')
            ]
            Image.bulk_create(images)

    def _write_to_csv(self, data_list: list[dict[str, Any]]):
        with open('files/notebooks.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.field_names)
            writer.writerows(data_list)


def main():
    url = 'https://rozetka.com.ua/notebooks/c80004/'
    scraper = RozetkaListingParser(url, 99)
    t1 = time.perf_counter()
    scraper.scrape()
    print(time.perf_counter() - t1, 'Waisted time')


if __name__ == '__main__':
    main()
