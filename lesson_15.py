# class Animal:
#     def speak(self):
#         raise NotImplementedError('Subclasses must implement this method')


class Cat:
    def speak(self):
        print('Meow')


class Dog:
    def speak(self):
        print('Gav')


class Cow:
    def speak(self):
        print('Mu')


def make_animal_speak(animal):
    print(animal.speak())


# cat = Cat()
# dog = Dog()
# cow = Cow()
#
# animals = [cat, dog, cow]
# for animal in animals:
#     animal.speak()
import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def display_area(shape):
    print(shape.area())


# circle = Circle(5)
# rectangle = Rectangle(4, 5)
#
# display_area(circle)
# display_area(rectangle)


from typing import Protocol, runtime_checkable


@runtime_checkable
class Flyable(Protocol):
    def fly(self):
        ...


class Bird:
    def fly(self):
        print('Bird fly')


class AirPlane:
    def fly(self):
        print('Airplane fly')


class Fish:
    def swim(self):
        print('Fish swim')


class FlyingFish(Fish):
    def swim(self):
        print('Flying fish swim')

    def fly(self):
        print('Flying fish fly')


def let_them_fly(objects: list):
    for obj in objects:
        obj.fly()


# bird = Bird()
# plane = AirPlane()
# print(isinstance(plane, Flyable))
# let_them_fly([bird, plane])
#
# fish = FlyingFish()
# let_them_fly([fish])

from typing import overload


@overload
def process_data(data: int) -> int:
    ...


@overload
def process_data(data: str) -> str:
    ...


def process_data(data):
    if isinstance(data, int):
        return data ** 2
    elif isinstance(data, str):
        return data.upper()
    else:
        raise TypeError('Unsupported type')


# x = process_data(10)
# print(x)
# string = process_data('hello')
# print(string)
# y = process_data(10.0)

import functools


class Processor:
    @functools.singledispatchmethod
    def process(self, data):
        raise NotImplementedError(f'No implementation for {type(data).__name__}')

    @process.register
    def _(self, data: int):
        print('Processing integer')
        return data ** 2

    @process.register
    def _(self, data: str):
        print('Processing string')
        return data.title()


# processor = Processor()
#
# print(processor.process(20))
# print(processor.process('hello world'))
# processor.process(10.0)


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary * 0.8

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError('Salary cannot be negative')
        self.__salary = salary


# employee = Employee('Taras', 30_000)
# print(employee._name)
# employee.set_salary(40_000)
# print(employee.get_salary())
# # print(employee._Employee__salary)
# print(employee.__salary)


class BankAccount:
    def __init__(self, account_number, balance = 0):
        self._account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposit cannot be negative, must be greater than 0')
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Withdraw cannot be negative, must be greater than 0')
        elif self.__balance < amount:
            raise ValueError('Withdraw cannot be above balance')
        else:
            self.__balance -= amount
            return self.__balance


# account = BankAccount(123456, 1000)
# print(account.get_account_number())
# print(account.get_balance())
# account._BankAccount__balance = 10_000
# print(account._BankAccount__balance)
# print(account.deposit(500))
# print(account.withdraw(300))



# def check_value(value):
#     if isinstance(value, int) or isinstance(value, float):
#         return True
#     return False


class Point:
    __slots__ = '__x', '__y'
    __WIDTH = 2

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coordinates(self):
        return self.__x, self.__y

    def set_coordinates(self, x, y):
        if self._check_value(x) and self._check_value(y):
            self.__x = x
            self.__y = y
        else:
            print('Invalid coordinates, should be int or float')

    @staticmethod
    def _check_value(value):
        if isinstance(value, int) or isinstance(value, float):
            return True
        return False

    def __setattr__(self, key, value):
        if key == '_Point__x' or key == '_Point__y':
            raise AttributeError
        self.__dict__[key] = value

    def __getattribute__(self, item):
        if item == '_Point__x' or item == '_Point__y':
            return f'Private attribute {item} cannot be accessed'
        else:
            return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print('No such attribute')



# point = Point(3, 4)
# # print(point.get_coordinates())
# point.set_coordinates(5, 6)
# print(point._check_value(7))
# print(Point._check_value(4))
# # setattr(Point, '__WIDTH', 5)
# # print(Point._Point__WIDTH)
# # type.__setattr__(point, '_Point__x', point)
# print('*' * 100)
# # print(point._Point__x)
# # print(point._Point__y)
# print('*' * 100)
# # point._Point__x = 10
# # point._Point__y = 20
# print(point.get_coordinates())

def factorial(number):
    if number == 0:
        return 1
    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

# class MathHelper:
#     @staticmethod
#     def factorial(number):
#         if number == 0:
#             return 1
#         result = 1
#         for i in range(1, number + 1):
#             result *= i
#
#         return result
#
#     @staticmethod
#     def is_prime(number):
#         if number <= 1:
#             return False
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 return False
#
#         return True

# math_helper = MathHelper()
# print(factorial(5))
# print(is_prime(5))

class Automobile:
    count = 0

    def __init__(self, brand, model):
        self._brand = brand
        self._model = model
        self.increase_count()

    @classmethod
    def increase_count(cls):
        cls.count += 1

    @classmethod
    def get_cars_count(cls):
        return cls.count


# car_1 = Automobile('Volvo', 100)
# # car_1.increase_count()
# car_2 = Automobile('Audi', 200)
# # car_2.increase_count()
#
#
# print(Automobile.count)


class Engine:
    def __init__(self, capacity: int, turbo: bool = False):
        self.capacity = capacity
        self.turbo = turbo

    def __repr__(self):
        return f'Engine(capacity={self.capacity}, turbo={self.turbo})'


class Car:
    def __init__(self, brand, model, color, engine):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine = engine

    @classmethod
    def camry(cls, color):
        engine = Engine(capacity=2500)
        return cls('Toyota', 'Camry', color, engine)

    @classmethod
    def audi_a6(cls, color):
        engine = Engine(capacity=2000, turbo=True)
        return cls('Audi', 'A6', color, engine)



# engine_1 = Engine(2000, True)
# engine_2 = Engine(3000)
#
# car_1 = Car('Toyota', 'Camry', engine_1)
# car_2 = Car('Audi', 'A6', engine_2)

# car_3 = Car.camry('Red')
# print(car_3.__dict__)
# car_4 = Car.audi_a6('Blue')
# print(car_4.__dict__)
