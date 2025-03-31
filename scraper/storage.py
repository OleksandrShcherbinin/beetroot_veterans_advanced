import csv

from base import DataStorage


class CsvStorage(DataStorage):
    def save(self, data: list[dict[str, str]], filename: str):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
