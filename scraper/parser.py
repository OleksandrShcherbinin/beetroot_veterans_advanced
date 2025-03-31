from base import Parser
from selectolax.parser import HTMLParser


class HtmlParser(Parser):
    def parse(self):
        return HTMLParser(self._response)


class RozetkaListingParser(HtmlParser):
    def parse(self):
        tree = super().parse()
        result_list = []
        items = [item for item in tree.css('.item')]
        for item in items:
            title = item.css('.goods-tile__title')
            information = title[0].text().split('/') if title else ''
            if not title:
                continue

            old_price = item.css('.goods-tile__price--old')
            new_price = item.css('.goods-tile__price-value')
            images = item.css('.goods-tile__picture img')
            image_links = [link.attrs.get('src') for link in images if link.attrs.get('src')]
            item = {
                'title': information[0].strip(),
                'monitor': information[1].strip() if len(information) > 1 else '',
                'cpu': information[2].strip() if len(information) > 2 else '',
                'memory': information[3].strip() if len(information) > 3 else '',
                'drive': information[4].strip() if len(information) > 4 else '',
                'old_price': (old := int(''.join([symbol for symbol in old_price[0].text() if symbol.isdigit()])) if old_price else ''),
                'new_price': (new := int(''.join([symbol for symbol in new_price[0].text() if symbol.isdigit()])) if new_price else ''),
                'discount': round((old - new) / old * 100) if old and new else 0,
                'images': image_links if image_links else [],
            }
            result_list.append(item)
        return result_list