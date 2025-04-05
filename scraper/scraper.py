from typing import Any

from base import Scraper
from response import TextResponse
from parser import RozetkaListingParser
from storage import CsvStorage


class RozetkaScraper(Scraper):

    def scrape(self) -> list[dict[str, Any]]:
        response = TextResponse(self._url, self._timeout)
        parser = RozetkaListingParser(response)
        parsed_data = parser.parse()
        storage = CsvStorage()
        storage.save(parsed_data, 'files/rozetka.csv')
        return parsed_data



def main() -> None:
    url = 'https://rozetka.com.ua/notebooks/c80004/'
    scraper = RozetkaScraper(url)
    scraper.scrape()


if __name__ == '__main__':
    main()
