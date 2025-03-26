# # # from collections import deque
# # # from urllib.parse import parse_qsl
# # #
# # # q = deque()
# # # q.append('Victor')
# # # q.append('Andriy')
# # # q.append('Oleksandr')
# # # q.appendleft('Anastasia')
# # # # print(q)
# # # # result = q.pop()
# # # # print(result)
# # # # result = q.popleft()
# # # # print(result)
# # #
# # # q = deque(maxlen=3)
# # # # q.append(1)
# # # # q.append(2)
# # # # q.append(3)
# # # # q.append(4)
# # # # print(q)
# # #
# # # q = deque([1, 2, 3, 4, 5, 6, 7])
# # # q.extend([1, 2, 3, 4])
# # # q.extendleft([1, 2, 3, 4])
# # # q.rotate(-4)
# #
# # # for i in q:
# # #     print(i)
# #
# # # print(q[3])
# #
# # from time import perf_counter, sleep
# # from collections import deque
# #
# #
# # class Progress:
# #     def __init__(self, total):
# #         self.total = total
# #         self.current = 0
# #         self.times = deque(maxlen=5)
# #
# #     def update(self):
# #         self.current += 1
# #         self.times.append(perf_counter())
# #         self.print_progress()
# #
# #     def print_progress(self):
# #         if len(self.times) > 1:
# #             elapsed = self.times[-1] - self.times[0]
# #             speed = (len(self.times) - 1) / elapsed if elapsed > 0 else 0
# #             remaining = (self.total - self.current) / speed if speed > 0 else float('inf')
# #         else:
# #             speed = 0
# #             remaining = float('inf')
# #
# #         print(f'Progress: {self.current}/{self.total}, Speed: {speed:.2f}, ETA: {remaining:.2f} sec', end='\r')
# #
# #
# # # progress = Progress(total=100)
# # # for _ in range(100):
# # #     sleep(0.1)
# # #     progress.update()
# #
# #
# # class Stack:
# #     def __init__(self):
# #         self.items = []
# #
# #     def push(self, item):
# #         self.items.append(item)
# #
# #     def pop(self):
# #         if not self.is_empty():
# #             return self.items.pop()
# #         raise IndexError('Stack is empty')
# #
# #     def is_empty(self):
# #         return len(self.items) == 0
# #
# #     def __len__(self):
# #         return len(self.items)
# #
# #     def __str__(self):
# #         return f"Stack[{', '.join(self.items[::-1])}]"
# #
# #
# # class Node:
# #     def __init__(self, value, next_node=None):
# #         self.value = value
# #         self.next_node = next_node
# #
# #
# # class Stack:
# #     def __init__(self):
# #         self.top = None
# #         self.size = 0
# #
# #     def push(self, item):
# #         new_node = Node(item, self.top)
# #         self.top = new_node
# #         self.size += 1
# #
# #     def pop(self):
# #         if self.top is None:
# #             raise IndexError('Stack is empty')
# #         item = self.top.value
# #         self.top = self.top.next_node
# #         self.size -= 1
# #         return item
# #
# #     def __len__(self):
# #         return self.size
# #
# #     def __str__(self):
# #         result = []
# #         current = self.top
# #         while current:
# #             result.append(str(current.value))
# #             current = current.next_node
# #         return f"Stack[{', '.join(result)}]"
# #
# #
# # # stack = Stack()
# # #
# # # stack.push('Document 1')
# # # stack.push('Document 2')
# # # stack.push('Document 3')
# # # stack.push('Document 4')
# # # result = stack.pop()
# # # print(result)
# # # print(stack)
# #
# # # from queue import LifoQueue
# # #
# # #
# # # lq = LifoQueue()
# # #
# # # lq.put('Document 1')
# # # lq.put('Document 2')
# # # lq.put('Document 3')
# # # lq.put('Document 4')
# # # lq.put('Document 5')
# # #
# # # print(lq.qsize())
# # #
# # # while lq.qsize():
# # #     print(lq.get())
# # # import bisect
# # #
# # # priority_schedule = [(1, 'python'), (2, 'sql'), (3, 'html')]
# # # bisect.insort(priority_schedule, (0.5, 'party'))
# # # print(priority_schedule)
# #
# # import heapq
# #
# # priority_queue = []
# # heapq.heappush(priority_queue, (2, 'code'))
# # heapq.heappush(priority_queue, (1, 'eat'))
# # heapq.heappush(priority_queue, (3, 'sleep'))
#
# # while priority_queue:
# #     priority, value = heapq.heappop(priority_queue)
# #     print(value)
#
# # data = [4, 1, 7, 3, 8, 5]
# # data = []
# # heapq.heappush(data, 4)
# # print(data)
# # heapq.heappush(data, 1)
# # print(data)
# # heapq.heappush(data, 7)
# # print(data)
# # heapq.heappush(data, 3)
# # print(data)
# # heapq.heappush(data, 8)
# # print(data)
# # heapq.heappush(data, 5)
# # print(data)
# # while priority_queue:
# #     priority, value = heapq.heappop(data)
# #     print(value)
# # print(data)
# # """
# #         1
# #       /   \
# #     3      5
# #       \      \
# #         4      7
# #                 \
# #                   8
# # """
#
# # from queue import PriorityQueue
# #
# # q = PriorityQueue()
# # q.put((2, 'sql'))
# # q.put((3, 'html'))
# # q.put((1, 'python'))
# #
# # print(q.get())
# # print(q.get())
# # print(q.get())
# import sys
#
# from lesson_21 import second
#
#
# # print(sys.getrecursionlimit())
# # sys.setrecursionlimit(1500)
#
# def recursive(value):
#     if value < 10:   # Базовий випадок
#         recursive(value + 1)  # Рекурсивний випадок
#
#     print(value)
#
#
# # recursive(1)
#
#
# def countdown(n):
#     print(n)
#     if n == 0:
#         return
#     countdown(n - 1)
#
#
# def countdown_iterative(n):
#     while n >= 0:
#         print(n)
#         n -= 1
#
#
# # countdown_iterative(10)
#
# def count_item_in_list(sequence: list[int], number: int) -> int:
#     count = 0
#     for i in sequence:
#         if i == number:
#             count += 1
#
#     return count
#
# my_list = [2, 3, 4, 5, 1, 6, 7, 1, 8, 9, 1, 10]
# # [3, 4, 5, 1, 6, 7, 1, 8, 9, 1, 10]
# # [4, 5, 1, 6, 7, 1, 8, 9, 1, 10]
# # [5, 1, 6, 7, 1, 8, 9, 1, 10]
# # [1, 6, 7, 1, 8, 9, 1, 10]  # + 1
# # [6, 7, 1, 8, 9, 1, 10]
# # [7, 1, 8, 9, 1, 10]
# # [1, 8, 9, 1, 10]  # + 1
# # [8, 9, 1, 10]
# # [9, 1, 10]
# # [1, 10] # + 1
# # [10]
# # []
# # result = count_item_in_list(my_list, 1)
# # print(result)
#
#
# def count_item_in_list_recursive(sequence: list[int], number: int) -> int:
#     if not sequence:
#         return 0
#
#     if sequence[0] == number:
#         return 1 + count_item_in_list_recursive(sequence[1:], number)
#
#     return count_item_in_list_recursive(sequence[1:], number)
#
#
# # result = count_item_in_list_recursive(my_list, 1)
# # print(result)
#
# # 5! = 1 * 2 * 3 * 4 * 5
#
# def factorial(number: int) -> int:
#     result = 1
#     for num in range(1, number + 1):
#         result *= num
#     return result
#
#
# # print(factorial(6))
#
#
# # def factorial_recursive(number: int) -> int:
# #     if number <= 1:
# #         return 1
# #     return number * factorial_recursive(number - 1)
#
#
# def factorial_recursive(number: int) -> int:
#     return 1 if number <= 1 else number * factorial_recursive(number - 1)
#
#
# # print(factorial_recursive(6))
# import math
#
# # print(math.factorial(6))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
def fibonacci(number: int) -> int:
    if number <= 1:
        return number
    first, second = 0, 1
    for i in range(2, number + 1):
        first, second = second, first + second

    return second

# print('*' * 100)
# print(fibonacci(100))
import functools
import time


@functools.lru_cache()
def fibonacci_recursive(number: int) -> int:
    if number <= 1:
        return number
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


# t1 = time.perf_counter()
# print(fibonacci_recursive(60))
# print(time.perf_counter() - t1)
import itertools

string = 'abcd'
# result = itertools.permutations(string)
# print(list(result))


def permutations_recursive(string: str) -> list[str]:
    if len(string) == 1:
        return [string]

    result = []
    for i in range(len(string)):
        first = string[i]
        rest = string[:i] + string[i + 1:]
        for mutation in permutations_recursive(rest):
            result.append(first + mutation)

    return result


print(permutations_recursive(string))

import sys
print(sys.getrecursionlimit())

