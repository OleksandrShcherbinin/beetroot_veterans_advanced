import os
import pathlib
from decimal import Decimal, localcontext

# file = open('files/log.txt')
# file.close()
#
# with open('files/log.txt') as file:
#     for line in file:
#         print(line)


# file_path = pathlib.Path('files/log.txt')
#
# file = file_path.open()
# print(file.read())
# file.close()

# with file_path.open() as file:
#     print(file.read())



# with os.scandir('files') as files:
#     for file in files:
#         print(file.name, file.stat())
#         print('*' * 80)

# with localcontext() as context:
#     context.prec = 2
#     print(Decimal(1) / Decimal(42))
#     print(0.3 + 0.3 + 0.3)
# print(dir(open('files/log.txt')))


class HelloContextManager:
    def __enter__(self):
        return 'Hello world!'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Leaving context')
        print(exc_type, exc_val, exc_tb)

# with HelloContextManager() as hello:
#     print(1, hello)
#     print('Some code 1')
#     print('Some code 2')
#     print('Some code 3')
#
# print('Out of context')


class MyFile:
    def __init__(
            self,
            name,
            mode
    ):
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print('Leaving context')


# with MyFile('files/log.txt', 'r') as file:
#     for line in file:
#         print(line)
#
# print('Out of context')


class Indenter:
    def __init__(self):
        self.level = -1

    def __enter__(self):
        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print('    ' * self.level + text)


# with Indenter() as indent:
#     indent.print('hi!')
#     with indent:
#         indent.print('hello')
#         with indent:
#             indent.print('bonjour')
#     indent.print('hey')


class Store:
    def __init__(self):
        self.products = []
        self.is_open = False

    def add_product(self, product):
        if not self.is_open:
            raise Exception('Store is closed')
        self.products.append(product)

    def get_product(self):
        if not self.is_open:
            raise Exception('Store is closed')
        if self.products:
            return self.products.pop()
        else:
            raise Exception('Store is empty')

    def open(self):
        self.is_open = True

    def close(self):
        self.is_open = False

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


# store = Store()
# with store:
#     store.add_product('Banana')
#     store.add_product('Apple')
#     store.add_product('Orange')
#     print(store.get_product())
#     print(store.get_product())
#     print(store.get_product())

# store.add_product('Apple')
# with Store() as store:
#     ...

import sqlite3


class DatabaseConnection:
    def __init__(self, database_url):
        self.database_url = database_url
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.database_url)
        self.cursor = self.connection.cursor()

    def execute(self, query):
        if self.cursor is None:
            raise Exception('No DB connectio')
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def commit(self):
        if self.connection:
            self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()
        else:
            print('No active connection')


class DatabaseManager:
    def __init__(self, database_url):
        self.database_url = database_url
        self.db_connection = None

    def __enter__(self):
        self.db_connection = DatabaseConnection(self.database_url)
        self.db_connection.connect()
        return self.db_connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting context')
        if exc_type is not None:
            print('Error')
        self.db_connection.close()


database_url = 'files/example.db'

with DatabaseManager(database_url) as db:
    db.execute(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY, name TEXT, age INTEGER
    )
    """
    )
    db.execute("INSERT INTO students (name, age) VALUES ('Alex', 43)")
    db.execute("INSERT INTO students (name, age) VALUES ('Inna', 18)")
    db.execute("INSERT INTO students (name, age) VALUES ('Andriy', 25)")
    db.commit()

