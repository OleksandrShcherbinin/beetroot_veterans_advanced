class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"{self.data} -> {getattr(self.next, 'data', '')}"


class LinkedListIterator:
    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        current = self.current
        self.current = self.current.next
        return current


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        return new_node

    def insert_after_node(self, previous_node, data):
        new_node = Node(data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def delete_after_node(self, previous_node):
        next_from_previous = previous_node.next
        previous_node.next = next_from_previous.next
        del next_from_previous

    def __iter__(self):
        current = self.head
        return LinkedListIterator(self)
        # while current:
        #     yield current
        #     current = current.next

    def __str__(self):
        return ' -> '.join(str(data) for data in self)


linked_list = LinkedList()
item1 = linked_list.append(1)
item2 = linked_list.append(2)
item3 = linked_list.append(3)
item4 = linked_list.append(4)
item5 = linked_list.append(5)
linked_list.insert_after_node(item4, 1.5)
linked_list.delete_after_node(item2)

# print(linked_list)
# for item in linked_list:
#     print(item)
#
# print('*' * 100)
# print(item3)
from dataclasses import dataclass, field
import uuid


@dataclass
class Address:
    region: str
    city: str
    street: str
    number: int
    zip_code: int
    country: str = field(default='Ukraine', repr=False)


def generate_id() -> str:
    return str(uuid.uuid4())


@dataclass(unsafe_hash=True)
class Student:
    first_name: str
    last_name: str
    age: int
    address: Address
    id: int = field(init=False, default_factory=lambda: generate_id(), compare=False)
    marks: list[int] = field(default_factory=list, compare=False, repr=False)
    _search: str = field(init=False, repr=False, compare=False)

    def __post_init__(self):
        self._search = f'{self.last_name}{self.address.city}'
        self._validate_age()

    def average_mark(self) -> float:
        return sum(self.marks) / len(self.marks)

    def _validate_age(self):
        if self.age > 150:
            raise ValueError('You are too old')


address = Address(
    'Cherkasy',
    'Cherkasy',
    'Shevchenko',
    100,
    18000
)

student_1 = Student(
    'Oleksandr',
    'Shcherbinin',
    151,
    address
)
student_1.marks.append(12)
student_1.marks.append(10)
student_1.marks.append(19)

address_2 = Address(
    'Cherkasy',
    'Cherkasy',
    'Shevchenko',
    100,
    18000,
    'France'
)
print(address == address_2)
student_2 = Student(
    'Oleksandr',
    'Shalashov',
    43,
    address_2
)
student_2.marks.append(12)
student_2.marks.append(12)
student_2.marks.append(12)

# student_1.age = 44

print(student_1)
print(student_2)
print(student_1.average_mark())
print(student_2.average_mark())
student_1.first_name = 'Alex'
# print(student_2.marks)


@dataclass(match_args=True)
class Data:
    a: int
    b: int


d = Data(1, 2)

match d:
    case Data(a, b):
        print(f'{a=},{b=}')
