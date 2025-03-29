import random
import time
# Slow sorting algorithms
# O(n^2)

# Selection sort

my_list = [7, 5, 1, 8, 3]
# [1, 5, 7, 8, 3]
# [1 | 3, 7, 8, 5]
# [1, 3 |  5, 7, 8]
# [1, 3, 5 | 7, 8]
# O(n^2)
def timer(function):
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = function(*args, **kwargs)
        print(time.perf_counter() - t1)
        return result
    return wrapper


@timer
def selection_sort(array: list[int]):
    for i in range(len(array) - 1):
        min_value = array[i]
        min_value_index = i

        for j in range(i + 1, len(array)):
            if min_value > array[j]:
                min_value = array[j]
                min_value_index = j

        if min_value_index != i:
            temporary = array[i]
            array[i] = array[min_value_index]
            array[min_value_index] = temporary

    return array


# list_to_sort = [3, 2, 1, 4, 5, 6, 9, 7, 0, 8]
# list_to_sort = [random.randint(1, 1000) for _ in range(1000)]
# result = selection_sort(list_to_sort)
# print(result)
# Buble sort
# O(n^2)
my_list_2 = [7, 5, 1, 8, 3]
# [5, 7, 1, 8, 3] | [5, 1, 7, 8, 3] | [5, 1, 7, 8, 3] | [5, 1, 7, 3, 8]
# [1, 5, 7, 3, 8] | [1, 5, 7, 3, 8] | [1, 5, 3, 7, 8]
# [1, 3, 5, 7, 8]

@timer
def bubble_sort(array: list[int]) -> list[int]:
    for i in range(len(array) - 1):
        already_sorted = True
        for j in range(len(array) - i - 1):

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


# list_to_sort = [3, 2, 1, 4, 5, 6, 9, 7, 0, 8]
# list_to_sort = [random.randint(1, 1000) for _ in range(1000)]
# result = bubble_sort(list_to_sort)
# print(result)

# Insertion sort
# O(n^2)

list_to_sort = [8, 4, 3, 7, 6]
# [4, 8, 3, 7, 6]
# [3, 4, 8, 7, 6]
# [3, 4, 7, 8, 6]
# [3, 4, 7, 6, 8]

@timer
def insertion_sort(array: list[int]) -> list[int]:
    for i in range(1, len(array)):

        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    return array


# list_to_sort = [random.randint(1, 1000) for _ in range(10000)]
# result = insertion_sort(list_to_sort)
# print(result)

# Merge sort
# O(n log n)
# list_to_sort = [38, 27, 43, 3, 9, 82, 10]
# [38, 27, 43] [3, 9, 82, 10]
# [38, 27, 43]
# [38] [27, 43]
# [38] [27] [43]
#########################################
# [3, 9] [82, 10]
# [3] [9]
# [82] [10]
# [3] [9] [82] [10]


def merge_sorted_list(left, right):
    i = 0
    j = 0
    merged_list = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            merged_list.append(right[j])
            j += 1

    merged_list += left[i:] + right[j:]

    return merged_list


def merge_sort(array: list[int]) -> list[int]:
    if len(array) < 2:
        return array

    middle = len(array) // 2

    return merge_sorted_list(
        left=merge_sort(array[:middle]),
        right=merge_sort(array[middle:])
    )


# list_to_sort = [3, 2, 1, 4, 5, 6, 9, 7, 0, 8]
# list_to_sort = [random.randint(1, 1000) for _ in range(10000)]
# t1 = time.perf_counter()
# result = merge_sort(list_to_sort)
# print(time.perf_counter() - t1)
# O(n log n)
def quick_sort(array: list[int]) -> list[int]:
    if len(array) > 1:

        pivot = array[random.randint(0, len(array) - 1)]

        low_values = [value for value in array if value < pivot]
        equal_values = [value for value in array if value == pivot]
        high_values = [value for value in array if value > pivot]

        array = quick_sort(low_values) + equal_values + quick_sort(high_values)

    return array


# list_to_sort = [3, 2, 1, 4, 5, 6, 9, 7, 0, 8]
list_to_sort = [random.randint(1, 1000) for _ in range(10000)]
t1 = time.perf_counter()
result = quick_sort(list_to_sort)
print(time.perf_counter() - t1)
# print(result)
