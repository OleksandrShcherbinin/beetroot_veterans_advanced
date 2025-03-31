from abc import ABC, abstractmethod
from typing import Any

import requests


class HttpResponse(ABC):
    def __init__(self, url: str, timeout: int = 5) -> None:
        self._url = url
        self._timeout = timeout

    @abstractmethod
    def get(self) -> requests.Response | None:
        try:
            return requests.get(self._url)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None


class Parser(ABC):
    def __init__(self, response: HttpResponse) -> None:
        self._response = response.get()

    @abstractmethod
    def parse(self):
        pass


class DataStorage(ABC):
    @abstractmethod
    def save(self, data, filename):
        pass


class Scraper(ABC):
    def __init__(self, url: str, storage: DataStorage, timeout: int = 5) -> None:
        self._url = url
        self._storage = storage
        self._timeout = timeout

    @abstractmethod
    def scrape(self):
        pass