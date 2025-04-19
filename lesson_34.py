from typing import Generator


def gen_string(string: str):
    for i in string:
        yield i


def gen_number(num: int):
    for i in range(1, num + 1):
        yield i


# gen_1 = gen_string('Python')
# gen_2 = gen_number(5)
#
# tasks = [gen_1, gen_2]
#
#
# while tasks:
#     task = tasks.pop(0)
#     try:
#         i = next(task)
#         print(i)
#         tasks.append(task)
#     except StopIteration:
#         pass


def generator():
    send_message = 'Ready to accept message'
    while True:
        message = yield send_message
        print('Message received', message)


# gen = generator()
# # next(gen)
# gen.send(None)
# gen.send('Hello')
# gen.send('world')
# gen.send('another hello')
# # gen.close()
# gen.throw(StopIteration)


def coroutine(function):
    def inner(*args, **kwargs):
        gen = function(*args, **kwargs)
        gen.send(None)
        return gen
    return inner


@coroutine
def average():
    count = 0
    total = 0
    avg = None
    while True:
        try:
            x = yield avg
        except StopIteration:
            print('Done')
            break
        else:
            if x is not None:
                count += 1
                total += x
                avg = round(total / count, 2)

    return avg


@coroutine
def delegator(coro):
    result = yield from coro
    print('Final average', result)


# gen = delegator(average())
#
# gen.send(100)
# gen.send(150)
# gen.send(200)
# gen.send(250)
# gen.send(300)
# gen.send(350)
# try:
#     gen.throw(StopIteration)
# except StopIteration:
#     pass
import asyncio


async def say_name(name: str):
    print(name)
    await asyncio.sleep(1)


async def hello():
    print('Hello')
    # await say_name('Oleksandr')
    task = asyncio.create_task(say_name('Inna'))
    await task
    print('Finish!!!')


# async def get_data():
#     print('Starting get data')
#     await asyncio.sleep(2)
#     print('Finished get data')
#     return {'data': 1000}
#
#
# async def print_numbers():
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(0.3)
#
#
# async def main():
#     task_1 = asyncio.create_task(get_data())
#     task_2 = asyncio.create_task(print_numbers())
#     value = await task_1
#     print(value)
#     await task_2


async def print_numbers():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.2)


async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('Seconds passed', count)

        count += 1
        await asyncio.sleep(1)


# async def main():
#     task_1 = asyncio.create_task(print_numbers())
#     task_2 = asyncio.create_task(print_time())
#     tasks = [task_1, task_2]
#     await asyncio.gather(*tasks)

import time
import requests
import aiohttp
import aiofiles


def get_file(url: str) -> requests.Response:
    response = requests.get(url, allow_redirects=True)
    return response


def write_image(response: requests.Response, num: int) -> None:
    file_name = response.url.split('/')[-1]
    file_name = file_name.split('.')
    file_name = file_name[1] + str(num) + '.' + file_name[2]
    with open(f'images/{file_name}', 'wb') as file:
        file.write(response.content)


def main():
    url = 'https://loremflickr.com/320/240?random=100'
    start = time.perf_counter()
    for i in range(10):
        response = get_file(url)
        write_image(response, i)
        print('Processed one image')

    end = time.perf_counter()
    print(f'TIME {end - start:.4f}')


def write_image_2(data: bytes) -> None:
    file_name = int(time.time() * 1000)
    with open(f'images/{file_name}.jpg', 'wb') as file:
        file.write(data)


async def write_image_3(data: bytes) -> None:
    file_name = int(time.time() * 1000)
    async with aiofiles.open(f'images/{file_name}.jpg', 'wb') as file:
        await file.write(data)


async def get_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()

        # write_image_2(data)
        await write_image_3(data)


async def main():
    url = 'https://loremflickr.com/320/240?random=100'

    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(get_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    # main()
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f'TIME {end - start:.4f}')
