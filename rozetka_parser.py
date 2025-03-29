from typing import Any

import requests
from selectolax.parser import HTMLParser


def get_response(url: str) -> str:
    response = requests.get(url, timeout=10)
    return response.text


def html_text_parser(html_string: str) -> dict[str, Any]:
    tree = HTMLParser(html_string)
    result_list = []
    items = [item for item in tree.css('.item')]
    for item in items:
        title = item.css('.goods-tile__title')
        information = title[0].text().split('/')
        old_price = item.css('.goods-tile__price--old price--gray')
        new_price = item.css('.goods-tile__price-value')
        images = item.css('.goods-tile__picture img')
        image_links = [link.attrs['src'] for link in images]
        result_list.append(
            {
                'title': information[0].strip(),
                'monitor': information[1].strip(),
                'cpu': information[2].strip(),
                'memory': information[3].strip(),
                'drive': information[4].strip(),
                'old_price': old_price,
                'new_price': new_price[0].text().replace('\\xa', ''),
                'images': image_links
            }
        )
    # breakpoint()

def main() -> None:
    url = 'https://rozetka.com.ua/notebooks/c80004/'
    html_string = get_response(url)
    html_text_parser(html_string)
    # Записати дані в CSV файл


if __name__ == '__main__':
    main()
