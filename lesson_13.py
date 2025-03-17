from datetime import datetime


def function():
    return 10



def function_2(func):
    return func



class Door:
    pass


# door_1 = Door()
# door_2 = Door()
#
# print(door_1)
# print(door_2)
#
# print(door_1 == door_2)
# print(door_1 is door_2)
#
# print(type(door_1))
# print(type(door_2))


class Warrior:
    health = 100
    level = 1

    def attack(self):
        print('Attack')

    def defend(self):
        print('Defend')


# warrior = Warrior()
#
# print(warrior.health)
# print(warrior.level)
# warrior.attack()
# warrior.defend()


class Cat:
    """ This is Cat class """
    species = 'mammal'
    paws = 4
    tail = 1
    eyes = 2

    def __init__(self, name, birth_year, color):
        self.name = name
        self.birth_year = birth_year
        self.color = color
        print(self.name, self.birth_year, self.color)

    def eat(self, food):
        print(self.name, f'Eats {food}')

    def age(self):
        return datetime.now().year - self.birth_year


tom = Cat('Tom', 2020, 'Grey')
oggy = Cat('Oggy', 2019, 'Blue')

cats = [tom, oggy]
tom.fights = 5

my_dict = {
    tom: 'Tom',
    oggy: 'Oggy'
}
print(id(tom))
print(id(oggy))
print(my_dict)

# for cat in cats:
#     cat.eat('Salo')

# print(tom.name)
# print(tom.age)
# print(tom.color)
# print(tom.paws)
# tom.eat('Fish')
# print('AGE', tom.age())
# oggy.eat('Fish')

# print(tom.__dict__)
# tom.eyes = 1
# print(tom.__dict__)
# print(Cat.__dict__)
# print(oggy.__dict__)

# oggy.color = 'Red'
# print(oggy.name)
# print(oggy.age)
# print(oggy.color)
# print(oggy.paws)


# class Example:
#     def __new__(cls, *args, **kwargs):
#         print('Instance creation')
#         instance = super().__new__(cls)
#         print(type(instance))
#         return instance
#
#     def __init__(self, value):
#         print('Init', value)
#         self.value = value
#         self.say_hello()
#
#     def say_hello(self):
#         print('Say hello')
#
#
# obj = Example('Value')
#
# obj.hello = 'Hello'
# setattr(obj, 'hello', 'Hello')
# obj.new_attr = 'New'
# result = getattr(obj, 'hello2', 'Hello2')
# print(result)
# print(obj.__dict__)
# del obj.hello
# delattr(obj, 'hello2')
# print(obj.__dict__)

# class Singleton:
#     instance = None
#     def __new__(klass, *objects, **kwobjects):
#         if not klass.instance:
#             print('Created new')
#             klass.instance = super().__new__(klass)
#             return klass.instance
#         else:
#             print('Returned existing instance')
#             return klass.instance
#
#     def __init__(self, value):
#         self.value = value
#
#
# print('*' * 100)
# singleton1 = Singleton(10)
# singleton2 = Singleton(20)
#
# print(singleton1 == singleton2)
# print(singleton1 is singleton2)
# print(id(singleton1))
# print(id(singleton2))

from typing import NamedTuple


class Point(NamedTuple):
    x: int
    y: int


point_1 = Point(3, 4)
point_2 = Point(5, 8)

print(point_1.x)
print(point_1.y)
print(point_1)
print('*' * 100)
print(point_2[0])
print(point_2[1])
