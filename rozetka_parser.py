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
            'title': information[0].strip(),
            'monitor': information[1].strip() if len(information) > 1 else '',
            'cpu': information[2].strip() if len(information) > 2 else '',
            'memory': information[3].strip() if len(information) > 3 else '',
            'drive': information[4].strip() if len(information) > 4 else '',
            'old_price': (old := int(''.join(
                [symbol for symbol in old_price[0].text() if
                 symbol.isdigit()])) if old_price else ''),
            'new_price': (new := int(''.join(
                [symbol for symbol in new_price[0].text() if
                 symbol.isdigit()])) if new_price else ''),
            'discount': round((old - new) / old * 100) if old and new else 0,
            'images': image_links if image_links else [],
        }
        result_list.append(item)
        print(len(result_list))
    # breakpoint()

def main() -> None:
    page = 'page=2/'
    url = 'https://rozetka.com.ua/notebooks/c80004/'
    html_string = get_response(url)
    html_text_parser(html_string)
    # Записати дані в CSV файл


if __name__ == '__main__':
    main()
