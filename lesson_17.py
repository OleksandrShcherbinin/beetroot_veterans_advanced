import math

from urllib3.util import resolve_cert_reqs


class Circle:
    def __init__(self, radius):
        self._radius = radius

    def _validate(self, value):
        if value <= 0:
            raise ValueError('Radius must be zero or positive')

    def get_radius(self):
        return self._radius

    def set_radius(self, value):
        self._validate(value)
        self._radius = value

    def del_radius(self):
        del self._radius

    radius = property(get_radius, set_radius, del_radius, "RADIUS")

    def get_diameter(self):
        return self._radius * 2

    diameter = property(get_diameter)

    def get_area(self):
        return math.pi * (self._radius ** 2)

    area = property(get_area)

    def __str__(self):
        return f'Circle {self.radius=} {self.diameter=} {self.area=}'


circle = Circle(10)
print(circle.__dict__)
print(circle.radius)
circle.radius = 30
print(circle)
# del circle.radius
print(circle.diameter)
print(circle.area)
# print(circle.get_radius())
# circle.set_radius(30)
# # circle.del_radius()
# print(circle)
# print(circle._radius)

class CircleModern:
    def __init__(self, radius):
        self._radius = radius

    def _validate(self, value):
        if value <= 0:
            raise ValueError('Radius must be zero or positive')

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._validate(value)
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return math.pi * (self._radius ** 2)

    def __str__(self):
        return f'Circle {self.radius=} {self.diameter=} {self.area=}'


print('*' * 100)
new_circle = CircleModern(10)
print(new_circle.radius)
new_circle.radius = 30
print(new_circle.radius)
print(new_circle.diameter)
print(new_circle.area)
print(new_circle)

import os
import hashlib


class User:
    salt = os.urandom(32)

    def __init__(self, email):
        self.email = email
        self.__password = None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = hashlib.pbkdf2_hmac(
            'sha256', value.encode('utf-8'), self.salt, 1000
        )
        print(self.__password)

    def login(self, password):
        our_password = hashlib.pbkdf2_hmac(
            'sha256', password.encode('utf-8'), self.salt, 1000
        )
        print(our_password)
        if our_password == self.password:
            print('Access granted!')



user = User('test@email.com')
print('*' * 100)
user.password = 'qwerty'
print(user.password)
user.login('qwerty')


class Point3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @classmethod
    def verify(cls, value):
        if not isinstance(value, int):
            raise TypeError('Point coordinates must be integers')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self.verify(value)
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self.verify(value)
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self.verify(value)
        self._z = value

    def __str__(self):
        return f'Point3D {self.x=}, {self.y=}, {self.z=}'


print('\n\n\n')
print('*' * 100)
point = Point3D(1, 2, 3)
print(point)
print(point.x)
print(point.y)
print(point.z)
point.x = 100
print(point)
print('\n\n\n')
print('*' * 100)


class IntegerDescriptor:
    def __set_name__(self, owner, name):
        print(owner)
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Value must be integer')
        setattr(instance, self.name, value)


class Point3D:
    x = IntegerDescriptor()
    y = IntegerDescriptor()
    z = IntegerDescriptor()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Point3D {self.x=}, {self.y=}, {self.z=}'


point = Point3D(1, 2, 3)
print(point)
print(point.x)
print(point.y)
print(point.z)
point.x = 100
print(point.__dict__)
print('\n\n\n')
print('*' * 100)
import re


class ModelField:
    def __init__(self, default=None):
        self.default = default

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, self.default)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class CharField(ModelField):
    def __init__(self, max_length = None, default = ''):
        super().__init__(default)
        self.max_length = max_length

    def __set__(self, instance, value):
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f'Max length is too long {self.max_length=}')
        super().__set__(instance, value)


class EmailField(CharField):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    def __set__(self, instance, value):
        if self.max_length is not None and len(value) > self.max_length:
            raise ValueError(f'Max length is too long {self.max_length=}')
        if not re.match(self.pattern, value):
            raise ValueError('Invalid email')
        super().__set__(instance, value)


class Profile:
    name = CharField(max_length=100)
    email = EmailField(max_length=50)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name=}, {self.email=}'


profile = Profile()
profile.name = 'Alex'
profile.email = 'test@email.com'
print('*' * 100)
print(profile)
print(profile.__dict__)


class LazyProperty:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, instance, owner):
        if not instance:
            print('No instance')
            return self

        value = self.function(instance)
        print('Setting value', value)
        setattr(instance, self.name, value)
        return value


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @LazyProperty
    def area(self):
        print('Calculating area')
        return math.pi * self._radius ** 2

    @LazyProperty
    def perimeter(self):
        print('Calculating perimeter')
        return self._radius * math.pi * 2


circle = Circle(4)
print('\n\n\n\n\n')
print('*' * 100)
print(circle.__dict__)
print(circle.area)
print(circle.__dict__)
print(circle.area)
print(circle.area)
