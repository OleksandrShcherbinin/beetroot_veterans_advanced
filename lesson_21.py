import math
from pprint import pprint


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]  # 10 operations
my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 4 operations
# my_list_2_1 = [1, 2, 3, 4, 5] # 1 operation
my_list_2_2 = [6, 7, 8, 9, 10]
# my_list_3_1 = [6, 7, 8]  # 1 operation
my_list_3_2 = [9, 10]
# my_list_4_1 = [9]  # 1 operation
my_list_4_2 = [10]  # 1 operation

number_of_elements = len(my_list_2)

print(my_list.count(5))


class MyList:
    def __init__(self):
        self._counter = 0
        self._container = []

    def append(self, element):
        self._container.append(element)
        self._counter += 1

    def __len__(self):
        return self._counter


max_binary_search_steps_mapping = {
    10: 4,
    100: math.log2(100),
    1000: math.log2(1000),
    10_000: math.log2(10000),
    100_000: math.log2(100000),
    1_000_000: math.log2(1000000),
    10_000_000: math.log2(10000000),
    10_000_000_000: math.log2(10000000000),
}

# pprint(max_binary_search_steps_mapping)


def binary_search(sequence, to_find):
    low = 0
    high = len(sequence) - 1
    steps = 0

    while low <= high:
        steps += 1
        middle = int((low + high) / 2)

        guess = sequence[middle]

        if guess == to_find:
            print('Completed in', steps)
            return middle

        if guess > to_find:
            high = middle - 1
        else:
            low = middle + 1

    return None


# O(1)
# O(log n)
# O(n)
# O(n log n)
# O(n^2)
# O(n^3)
# O(2^n)
# O(n!)


def get_list_length(sequence):  # O(1)
    return len(sequence)


# print(my_list[5])  # O(1)
#
# n = 100
# for i in range(n):  # O(n)
#     print(i)

counter = 0
n = 100
for i in range(n):  # O(n^2)
    for j in range(n):
        # print(i + j)
        counter += 1


# print(counter)
counter = 0
n = 100
for i in range(n):
    for j in range(n):
        # print(i + j)
        counter += 1
        for k in range(n):
            # print(i + k)
            counter += 1

print(counter)


from itertools import permutations


def generate_permutations(input_list):
    return [list(p) for p in permutations(input_list)]


# print(generate_permutations([1, 2, 3, 4]))
#
# print(1 * 2 * 3 * 4 * 5 * 6 * 7)
from time import perf_counter
import matplotlib.pyplot as plot


def question1(first_list: list[int], second_list: set[int]) -> list[int]:
    res: list[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


x = []
y = []

for i in range(1, 10001):
    first = [i for i in range(i)]
    second = [i for i in range(i)]
    x.append(i)
    t1 = perf_counter()
    question1(first, second)
    t2 = perf_counter()
    y.append(t2 - t1)

fig, ax = plot.subplots()
ax.plot(x, y, color='blue')
fig.savefig('files/time_complexity_set.png')
