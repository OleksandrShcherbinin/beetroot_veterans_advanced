def shout(text: str) -> str:
    return text.upper()


def whisper(text: str) -> str:
    return text.lower()


def greet(function):
    greeting = function('Hi this is greet function!')
    print(greeting)


# greet(shout)
# greet(whisper)


def summation(number, function):
    total = 0
    for num in range(1, number + 1):
        total += function(num)

    return total


def square(number):
    return number * number


def cube(number):
    return number ** 3


# print(summation(5, square))
# print(summation(3, cube))


# def outer_function():
#     print('Outer')
#     def inner_function():
#         return 'This is inner function'
#
#     return inner_function


def factorial(number):
    if not isinstance(number, int):
        raise TypeError('Number must be integer')
    if number < 0:
        raise ValueError('Number must be zero or positive')

    def inner_factorial(number):
        if number <= 1:
                return 1
        total = 1
        for i in range(1, number + 1):
            total *= i
        return total

    return inner_factorial(number)


def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


# closure = outer_function(10)
#
# print(closure(5))
# print(closure(30))
# print(closure(100))


def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment


# closure = counter()
#
# print(closure())
# print(closure())
# print(closure())
# print(closure())
# print(closure())


def person(name: str, age: int):
    _name = name
    _age = age

    def get_name():
        return _name

    def get_age():
        return _age

    def set_name(new_name: str):
        nonlocal _name
        _name = new_name

    def set_age(new_age: int):
        nonlocal _age
        _age = new_age

    return {
        'get_name': get_name,
        'get_age': get_age,
        'set_name': set_name,
        'set_age': set_age
    }

# person_1 = person('Borys', 30)
# print(person_1)
# person_2 = person('Halyna', 18)
# print(person_2)
#
# print(person_1['get_name']())
# print(person_1['get_age']())
#
# person_1['set_age'](31)
# print(person_1['get_age']())
# print(person_1['get_age']())
import csv
import json
from pprint import pprint

import requests


def write_to_json(data):
    with open('files/data.json', 'w') as file:
        json.dump(data, file, indent=4)


def write_to_csv(data):
    with open('files/data.csv', 'w') as file:
        writer = csv.writer(file, )
        for item in data:
            row = [item['id'], item['name'], item['email']]
            writer.writerow(row)


def write_to_pdf(data):
    print(f'Process data {data}')


def fetch_data(function):
    data = requests.get('https://jsonplaceholder.typicode.com/users')
    json_data = data.json()
    function(json_data)


# fetch_data(write_to_json)
# fetch_data(write_to_csv)
# fetch_data(write_to_pdf)


def add(x, y):
    return x + y


def curried_add(x):
    def curry(y):
        return add(x, y)
    return curry


# add_five = curried_add(5)
#
# result = add_five(10)
# print(result)
# result = add_five(3)
# print(result)
# result = add_five(12)
# print(result)
# result = add_five(1)
# print(result)
import functools


# add_five = functools.partial(add, 5)
# result = add_five(10)
# print(result)


def log_message(level, message):
    print(f'[{level.upper()}] {message}')

#
# info_log = functools.partial(log_message, 'info')
# error_log = functools.partial(log_message, 'error')
# debug_log = functools.partial(log_message, 'debug')
#
# info_log('Application started')
# info_log('Application started')
# info_log('Application started')
# info_log('Application started')
# error_log('Error happened')
# debug_log('This is debug')
#
# info_log('Application started')
# info_log('Application started')
# info_log('Application started')

# def order_pizza(size, crust, toppings):
#     return f"Pizza order, size: {size}, crust: {crust}, toppings: {', '.join(toppings)}"
#
#
# large_pizza = functools.partial(order_pizza, 'Large')
# small_pizza = functools.partial(order_pizza, 'Small')
#
# print(large_pizza('Thin', ['Salami', 'Mushrooms']))
# print(small_pizza('Thin', ['Salami', 'Mushrooms']))


def my_decorator(function):
    def wrapper():
        print('Before function')
        function()
        print('After function')
    return wrapper

# say_hello = my_decorator(say_hello)
# # print(say_hello)
# say_hello()


from datetime import datetime


def not_during_the_night(function):

    def wrapper():
        if 7 <= datetime.now().hour < 22:
            function()
        else:
            pass
    return wrapper


# say_hello = not_during_the_night(say_hello)
# say_hello()
# say_python = not_during_the_night(say_python)
# say_python()


def do_twice(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        function(*args, **kwargs)
    return wrapper


@not_during_the_night
def say_hello():
    print('Hello')


@do_twice
def say_python():
    print('Python')


@do_twice
def say_hello_to_person(name: str, gender: str):
    if gender == 'F':
        print(f'Good afternoon {name.title()}')
    else:
        print(f'Hello {name}')


@do_twice
def say_hello_to(name: str):
    print(f'Hello {name}')


# say_hello_to_person('Oleksandr', 'M')
# say_hello_to('Inna')
import functools


def universal_decorator(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        # Do something before
        result = function(*args, **kwargs)
        # Do something after
        result = result + '!'
        return result
    return wrapper


# @universal_decorator
# def greet(name):
#     return f'Hi {name}'

#
# print(greet)

import time


def timer(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        print('Timer')
        result = function(*args, **kwargs)
        finish = time.perf_counter()
        run_time = finish - start
        print(f'Finished {function.__name__} in {run_time:4f} secs')
        return result

    return wrapper


def debug(function):

    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f'{key}={value}' for key, value in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {function.__name__} ({signature})')
        result = function(*args, **kwargs)
        print(f'{function.__name__} returned {result}')
        return result

    return wrapper


@debug
@timer
def waste_some_time(num_times):
    total = 0
    for _ in range(num_times):
        total += sum([i ** 2 for i in range(10000)])
    return total


# waste_some_time(2)


def repeat(num_times):

    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                value = function(*args, **kwargs)
                print(value)
        return wrapper

    return decorator




# @repeat(10)
# def greet(name):
#     return f'Hi {name}'


def box_print(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        print('-' * (len(result) + 4))
        print('|', result, '|')
        print('-' * (len(result) + 4))
        return result
    return wrapper


@box_print
def greet(name):
    return f'Hi {name}'


# greet('Hello world')


def memoize(function):
    memo = {}
    def wrapper(*args, **kwargs):
        print(memo)
        if args in memo:
            print('From cache')
            return memo[args]
        else:
            result = function(*args, **kwargs)
            memo[args] = result
            print('From function')
            return result


    return wrapper


@functools.cache
def add_two(x, y):
    return x + y


print(add_two(1, 1))
print(add_two(1, 2))
print(add_two(1, 3))
print(add_two(1, 1))

# @box_print
# def say_hello_world_2():
#     return 'Hello world!!!'

class Page:
    url = 'https://'


class Browser:
    width = 1000
    height = 800
    page = Page()

    def get_url(self):
        pass

    def post_form(self):
        pass

    def close(self):
        pass

    def reload(self):
        pass