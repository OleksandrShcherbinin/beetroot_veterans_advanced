import time


class LazyObject:
    def __init__(self):
        self._data = None

    def _load_data(self):
        print('Loading data ...')
        time.sleep(2)
        self._data = 'Expensive data'

    def __getattribute__(self, item):
        if item == '_data' and super().__getattribute__('_data') is None:
            self._load_data()
        return super().__getattribute__(item)



# lazy = LazyObject()
# print(lazy._data)
# print(lazy._data)


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __setattr__(self, key, value):
        print(key, value)
        if key == 'email':
            value = value.lower()
        super().__setattr__(key, value)

    def __repr__(self):
        return f'{self.name}, {self.email}'

    def __str__(self):
        return f'User {self.name}, {self.email}'


# user = User('Petro', 'TEST@EMAIL.COM')
#
# # print(user)
# print(repr(user))

class Logger:
    def __init__(self, filename):
        print('Open file')
        self.file = open(filename, 'w', encoding='utf-8')

    def log(self, message):
        print('Writing log')
        self.file.write(f'{message}\n')

    def __del__(self):
        print('Closing file')
        self.file.close()


# logger = Logger('files/log.txt')
# logger.log('This is log message')
# logger.log('This is log message 2')
# logger.log('This is log message 3')


class Counter:
    def __init__(self):
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.counter


# counter = Counter()
#
# print(counter())
# print(counter())
# print(counter())


class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __call__(self, *args, **kwargs):
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        return value


# fibonacci = Fibonacci()
#
# for _ in range(20):
#     print(fibonacci(), end=' ')


class RangeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f'Value {value} out of range')
        return value

#
# validator = RangeValidator(0, 120)
#
# print(validator(-10))


class Retry:
    def __init__(self, attempts = 3, delay = 1):
        self.attempts = attempts
        self.delay = delay

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            for i in range(self.attempts):
                try:
                    return function(*args, **kwargs)
                except Exception as error:
                    print(f'Attempt {i}, filed {error}')
                    time.sleep(self.delay)
            return None
        return wrapper


def retry(attempts = 3, delay = 1):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    return function(*args, **kwargs)
                except Exception as error:
                    print(f'Attempt {i}, filed {error}')
                    time.sleep(delay)
            return None
        return wrapper
    return decorator


# @Retry(attempts=2, delay=2)
@retry(attempts=2, delay=2)
def some_function():
    print('Function call')
    return 1 / 0


# some_function()


def class_decorator(cls):
    cls.extra_attribute = 'Extra'
    return cls


@class_decorator
class MyClass:
    pass


class Stack:
    def __init__(self):
        self.count = 0
        self.items = []

    def push(self, item):
        self.items.append(item)
        self.count += 1

    def pop(self):
        self.count -= 1
        return self.items.pop()

    def __len__(self):
        return self.count


# stack = Stack()
# stack.push('apple')
# stack.push('banana')
# stack.push('orange')
# stack.pop()
#
# print(len(stack))


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __floordiv__(self, other):
        result = self.__truediv__(other)
        return result.numerator // result.denominator

    def __mod__(self, other):
        floor_result = self.__floordiv__(other)
        return self - other * Fraction(floor_result, 1)


    def __str__(self):
        return f'{self.numerator}/{self.denominator}'


# f1 = Fraction(1, 2)
# f2 = Fraction(2, 3)
#
# print(f1 + f2)
# print(f1 - f2)
# print(f1 * f2)
# print(f1 / f2)
# print(f1 // f2)
# print(f1 % f2)
#
# print('*' * 100)
# from fractions import Fraction
#
#
# f1 = Fraction(1, 2)
# f2 = Fraction(2, 3)
#
# print(f1 + f2)
# print(f1 - f2)
# print(f1 * f2)
# print(f1 / f2)
# print(f1 // f2)
# print(f1 % f2)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.grade == other.grade

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.grade != other.grade

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.grade < other.grade

    def __le__(self, other):
        if isinstance(other, Student):
            return self.grade <= other.grade

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.grade > other.grade

    def __ge__(self, other):
        if isinstance(other, Student):
            return self.grade >= other.grade

student_1 = Student('Inna', 90)
student_2 = Student('Andriy', 88)

print(student_1 == student_2)
print(student_1 != student_2)
print(student_1 < student_2)
print(student_1 <= student_2)
print(student_1 >= student_2)
print(student_1 >= student_2)
