import asyncio
import sys
import time

import httpx
import uvloop
from selectolax.parser import HTMLParser

from rozetka_db import Price, Product, Image

COUNTER = 0
USER_AGENT = {'User-agent': 'Googlebot-Image/1.0'}


def parse(html_string: str) -> None:
    global COUNTER
    COUNTER += 1

    tree = HTMLParser(html_string)
    result_list = []
    items = [item for item in tree.css('.item')]
    for item in items:
        title = item.css('.tile-title')
        if not title:
            continue

        information = title[0].text().split('/')
        old_price = item.css('.old-price')
        new_price = item.css('.price')
        images = item.css('.tile-image')
        image_links = [link.attrs.get('src') for link in images if
                       link.attrs.get('src')]
        item = {
            'id': COUNTER,
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


async def worker(
        que: asyncio.Queue,
        worker_number: int,
        session: httpx.AsyncClient
):
    while not que.empty():
        url = await que.get()
        print(f'[Request in {worker_number}] [queue size {que.qsize()}] -> {url}')
        try:
            response = await session.get(url, timeout=10, headers=USER_AGENT)
            parse(response.text)
        except httpx.NetworkError as error:
            print('Network error', error)
            await que.put(url)
        except Exception as error:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print('Some error', error, exc_tb.tb_lineno)


async def main() -> None:
    url = 'https://rozetka.com.ua/notebooks/c80004/'
    workers = 99
    urls_que = asyncio.Queue()
    for num in range(1, workers + 1):
        if num == 1:
            urls_que.put_nowait(url)
        else:
            urls_que.put_nowait(f'{url}page={num}/')

    session = httpx.AsyncClient()
    tasks = []

    for worker_number in range(workers):
        task = asyncio.create_task(worker(urls_que, worker_number, session))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    uvloop.install()
    start = time.perf_counter()
    asyncio.run(main())
    finish = time.perf_counter()
    print(f'Scraping done in {finish - start:.4f} seconds')
