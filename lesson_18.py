#
# for i in [1, 2, 3, 4, 5]:
#     print(i)
#
#
# for i in 'hello':
#     print(i)
#
#
# for i in 1000:
#     print(i)


# print(dir([1, 2, 3, 4, 5]))
# print('*' * 100)
# print(dir('hello'))
# print('*' * 100)
# print(dir(1000))


# list_of_numbers = [1, 2, 3, 4, 5]
# index = 0
# while index < len(list_of_numbers):
#     print(list_of_numbers[index])
#     index += 1


# set_of_numbers = {5, 4, 3, 2, 1}
# iterator = iter(set_of_numbers)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# iterator = iter(set_of_numbers)
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break
# for obj in set_of_numbers:
#     print(obj)

def for_loop(iterable):
    # iterator = iter(iterable)
    iterator = iterable.__iter__()
    next_element_exists = True
    while next_element_exists:
        try:
            # element_from_iterator = next(iterator)
            element_from_iterator = iterator.__next__()
            print(element_from_iterator)
        except StopIteration:
            next_element_exists = False


set_of_numbers = {5, 4, 3, 2, 1}

# for_loop(set_of_numbers)

# for obj in set_of_numbers:
#     print(obj)

class LimitIterator:
    def __init__(self, limit):
        self._number = -1
        self._limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self._number >= self._limit:
            raise StopIteration

        self._number += 1
        return self._number


limit_iterator = LimitIterator(5)
#
# for item in limit_iterator:
#     print(item)
import time


class CountDown:
    def __init__(self, start):
        self.count = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.count <= 0:
            print('Launch...')
            raise StopIteration
        current = self.count
        time.sleep(0.5)
        self.count -= 1
        return current


# for number in CountDown(5):
#     print(number, end=' ')


class InfiniteIterator:
    def __init__(self, initial_number):
        self.count = initial_number

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        return self.count


# for i in InfiniteIterator(2):
#     print(i)
#     if i > 7000:
#         break

# for i in range(10.5):
#     print(i)

class FloatRange:
    def __init__(self, start=0.0, end=0.0, step=1.0):
        self.start = start
        self.end = end
        self.step = step

    def __next__(self):
        if self.value + self.step > self.end:
            raise StopIteration

        self.value += self.step
        return self.value

    def __iter__(self):
        self.value = self.start - self.step
        return self


# float_range = FloatRange(0.0, 10.0, 0.2)
# for item in float_range:
#     print(item)

class FibonacciIterator:
    ZERO = 0
    ONE = 1
    counter = 0

    def __init__(self, position):
        self._position = position
        self._previous = self.ONE
        self._before_previous = self.ZERO
        self._number = 0

    def __iter__(self):
        if self._position < 0:
            raise ValueError('Should be not negative')
        return self

    def __next__(self):
        if self.counter == self._position:
            raise StopIteration

        self.counter += 1

        if self._position == 0 or self.counter == 1:
            return self.ZERO
        if self._position == 1 or self.counter == 2:
            return self.ONE

        self._number = self._before_previous + self._previous
        self._before_previous = self._previous
        self._previous = self._number
        return self._number


# for item in FibonacciIterator(20):
#     print(item, end=', ')


class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def __repr__(self):
        return f"Book(title='{self._title}', author='{self._author}')"


class BookCollectionIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration


class BookCollection:
    def __init__(self):
        self._books = []

    def add(self, title, author):
        self._books.append(Book(title, author))

    def __iter__(self):
        return BookCollectionIterator(self._books)


collection = BookCollection()

collection.add('1984', 'George Orwell')
collection.add('Kobzar', 'Taras Schevchenko')
collection.add('Forest Song', 'Lesia Ukrainka')

# for book in collection:
#     print(book)


def get_from_list():
    for i in range(3):
        yield i


# generator = get_from_list()
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

def infinite():
    num = 0
    while True:
        yield num
        num += 1
        yield 'Second yield'


# inf = infinite()
# print(next(inf))
# print(next(inf))
# print('*' * 100)
# print(next(inf))
# print(next(inf))
# print('*' * 100)
# print(next(inf))
# print(next(inf))
# print('*' * 100)
# print(next(inf))
# print(next(inf))
# print('*' * 100)
# print(next(inf))
def limited(limit: int):
    num = 0
    while num <= limit:
        yield num
        num += 1


# for i in limited(10):
#     print(i)
import sys
import cProfile


# squares = [number ** 2 for number in range(100_000)]
# # print(squares)
# print(sys.getsizeof(squares))
#
squares_generator = (number ** 2 for number in range(100_000_000))
# print(sys.getsizeof(squares_generator))
#
# squares_sum = sum(number ** 2 for number in range(100_000_000))
# print(squares_sum)

# cProfile.run('sum([number ** 2 for number in range(100_000)])')
# cProfile.run('sum(number ** 2 for number in range(100_000))')


def range_generator(start, stop, step):
    counter = start
    while counter <= stop:
        yield counter
        counter += step

# generator = range_generator(0, 10, 0.5)
# for item in generator:
#     print(item)
#
# print('*' * 100)
# generator = range_generator(0, 10, 0.5)
# for item in generator:
#     print(item)

# def ip_generator():
#     for i in range(256):
#         for j in range(256):
#             for k in range(256):
#                 for n in range(256):
#                     yield f'{i}.{j}.{k}.{n}'


# for i, ip in enumerate(ip_generator()):
#     print(ip)
#     if i > 1000:
#         break


def restartable():
    num = 0
    while True:
        value = (yield num)
        if value == 'restart':
            num = 0
        if value == 'stop':
            break
        else:
            num += 1


# restart = restartable()
#
# for i in restart:
#     print(i)
#     if i == 10:
#         # restart.send('stop')
#         # restart.close()
#         restart.throw(ValueError('This limit'))
# import csv
#
#
# file_name = 'files/Gross-domestic-product-March-2022-quarter-visualisation-csv.csv'
#
#
# lines = (line for line in open(file_name))
# list_rows = (row for row in csv.reader(lines, quotechar='"', delimiter=','))
# columns = next(list_rows)
# industries_dicts = (dict(zip(columns, data)) for data in list_rows)
#
# incomes = (
#     float(industries_dict['Amount'])
#     for industries_dict in industries_dicts
# )
# print(sys.getsizeof(incomes))
# total = sum(incomes)
# print('Total', total)


def accumulate(values):
    total = 0
    for value in values:
        total += value
        yield total
    return total


def delegator(values):
    final_sum = yield from accumulate(values)
    print('Final sum', final_sum)


# del_generator = delegator([1, 2, 3])
# for intermediate_sum in del_generator:
#     print('Intermediate sum', intermediate_sum)
import os


def read_log_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line


def aggregate_log(log_paths):
    for path in log_paths:
        yield from read_log_file(path)


def find_log_files(directory, extension='.log'):
    files_paths = []
    for file_name in os.listdir(directory):
        if file_name.endswith(extension):
            full_path = os.path.join(directory, file_name)
            files_paths.append(full_path)

    return files_paths


logs_dir = 'logs'
logs_to_read = find_log_files(logs_dir)
# print(logs_to_read)


for line in aggregate_log(logs_to_read):
    if '[ERROR]' in line:
        print(line)
