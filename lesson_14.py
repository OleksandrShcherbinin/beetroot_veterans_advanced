class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello! I am {self.name}'


class Son(Parent):
    def additional_method(self):
        return 'Method of son class'


class Daughter(Parent):
    def additional_method(self):
        return 'Method of daughter class'


# obj = Child('Child')
# print(obj.name)
# print(obj.greet())
# print(obj.additional_method())

class A:
    def method_a(self):
        return 'Method A'


class B:
    def method_b(self):
        return 'Method B'


class C(A, B):
    def method_c(self):
        return 'Method C'


# c_obj = C()
# print(c_obj.method_c())
# print(c_obj.method_b())
# print(c_obj.method_a())

class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Hello! I am {self.name}'


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def additional_method(self):
        return 'Method of daughter class'

    def greet(self):
        result = super().greet()
        return f'{result}. Nice to meet you! My age is {self.age}'

# parent = Parent('Name')
#
# child = Child('Son', 10)
# print(child.greet())


class SpecialString(str):
    def upper_lower(self):
        return ''.join(
            [
                symbol.upper() if i % 2 == 0 else symbol.lower()
                for i, symbol in enumerate(self)
            ]
        )


# my_string = SpecialString('Hello world! I love python')
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.upper_lower())
from enum import Enum


class FuelType(Enum):
    GASOLINE = 'Gasoline'
    DIESEL = 'Diesel'
    GAS = 'Liquefied Gas'


class Color(Enum):
    RED = 'REd'
    BLUE = 'Blue'
    GREEN = 'Green'
    BLACK = 'Black'
    WHITE = 'White'


class Engine:
    def __init__(self, cylinders, capacity, fuel_type):
        self.cylinders = cylinders
        self.capacity = capacity
        self.fuel_type = fuel_type

    def start(self):
        print('Engine starts')

    def stop(self):
        print('Engine stops')


class Car:
    wheels_number = 4

    def __init__(self, color, model, price):
        self.color = color
        self.model = model
        self.price = price
        self.engine = Engine(8, 4000, FuelType.DIESEL)

    def go(self):
        print('Car goes')

    def stop(self):
        print('Car stops')


engine = Engine(8, 4000, FuelType.DIESEL)

car = Car(Color.RED, 'BMW', 50_000)

# print(car.engine.capacity)
# print(car.engine.fuel_type)
# car.engine.start()
# car.go()
# car.stop()
# car.engine.stop()

from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def work(self):
        pass


class CarDriver(Employee):
    def work(self):
        print('Car driver drives')


class Waiter(Employee):
    def work(self):
        print('Serves food and drinks')


class DataProcessor(ABC):

    def process(self):
        data = self.load_data()
        transformed_data = self.transform_data(data)
        self.save_data(transformed_data)

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def transform_data(self, data):
        pass

    @abstractmethod
    def save_data(self, transformed_data):
        pass


class CSVProcesor(DataProcessor):

    def load_data(self):
        print('Loading data from csv')
        return ['row1', 'row2', 'row3']

    def transform_data(self, data):
        print('Transform data')
        return [row.upper() for row in data]

    def save_data(self, transformed_data):
        print('Saving data CSV')
        print(transformed_data)


class JSONProcesor(DataProcessor):

    def load_data(self):
        print('Loading data from json')
        return {'key1': 'value1', 'key2': 'value2'}

    def transform_data(self, data):
        print('Transform data')
        return {key: value.upper() for key, value in data}

    def save_data(self, transformed_data):
        print('Saving data JSON')
        print(transformed_data)


# csv_processor = CSVProcesor()
# csv_processor.process()


# class Square:
#     def __init__(self, side_length):
#         self.side_length = side_length
#
#     def area(self):
#         return self.side_length ** 2
#
#     def perimeter(self):
#         return self.side_length * 4


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# square = Square(10)
# print(square.area())
# print(square.perimeter())


class SurfaceAreaMixin:
    def surface_area(self):
        surface_area = 0
        for surface in self.surfaces:
            surface_area += surface.area(self)

        return surface_area

class Cube(SurfaceAreaMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.surfaces = [
            Square,
            Square,
            Square,
            Square,
            Square,
            Square,
        ]

    def volume(self):
        return self.length ** 3


cube = Cube(10)
print(cube.surface_area())
# print(cube.volume())
# print(cube.area())
# perimeter = super(Cube, cube).perimeter()
# print(perimeter)


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return (self.base * self.height) / 2


class RightPyramid(Triangle, Square):
# class RightPyramid(Square, Triangle):
    def __init__(self, base, height):
        super().__init__(base, height)


# pyramid = RightPyramid(3, 4)
# print(pyramid.base)
# print(pyramid.height)
# print(RightPyramid.__mro__)


class A:
    def __init__(self):
        print('A')
        super().__init__()


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C:
    def __init__(self):
        print('C')
        super().__init__()


class Forward(B, C):
    def __init__(self):
        print('Forward')
        super().__init__()


class Backward(C, B):
    def __init__(self):
        print('Backward')
        super().__init__()


# forward = Forward()
# print('*' * 100)
# backward = Backward()


class A:
    def show(self):
        print('A')


class B(A):
    def show(self):
        print('Before B')
        super().show()
        print('After B')


class C(A):
    def show(self):
        print('Before C')
        super().show()
        print('After C')


class D(B, C):
    def show(self):
        print('Before D')
        super().show()
        print('After D')


  #    A
  #  /   \
  # B     C
  #   \  /
  #    D

# d = D()
#
# d.show()
# print(D.__mro__)


class LoggingMixin:
    def log(self, action):
        print(f'[LOG]: {self.__class__.__name__}: {action}')


class User:
    def __init__(self, name):
        self.name = name


class Admin(User, LoggingMixin):
    def delete_user(self, user):
        print(f'Admin {self.name} deleted {user.name}')
        self.log(f'deleted {user.name}')


class Moderator(User, LoggingMixin):
    def mute_user(self, user):
        print(f'Moderator {self.name} muted {user.name}')
        self.log(f'muted {user.name}')


# admin = Admin('Yevhen')
# moderator = Moderator('Borys')
# user = User('Inna')
#
# moderator.mute_user(user)
# admin.delete_user(user)
