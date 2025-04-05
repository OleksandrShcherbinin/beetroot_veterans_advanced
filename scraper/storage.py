import csv
from typing import Any

from base import DataStorage


class CsvStorage(DataStorage):
    def save(self, data: list[dict[str, Any]], path: str) -> None:
        with open(path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
