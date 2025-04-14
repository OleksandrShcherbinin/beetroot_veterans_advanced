import math
import random
import time
from multiprocessing import Process, Pool, Queue, set_start_method, Lock, Manager
from concurrent.futures import ProcessPoolExecutor, as_completed
from selectolax.parser import HTMLParser


def worker(proc_number, shared_list, shared_dict):
    print('Hello from process!!!')
    result = random.randint(1, 100)
    time.sleep(random.random())
    shared_list.append(result)
    shared_dict[proc_number] = result
    print(f'Process {proc_number}, result {result!r}')



def square(x, lock):
    with lock:
        print(x * x)


def fibonacci_recursive(number: int) -> int:
    if number <= 1:
        return number
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number - 2)


def compute_sqrt(x):
    print('Process computes number', x)
    fibonacci_recursive(35)
    return math.sqrt(x)


def extract_title(html_string: str) -> str:
    tree = HTMLParser(html_string)
    title = tree.css('title')
    if not title:
        return ''
    return title[0].text().strip()


if __name__ == '__main__':
    # freeze_support()
    # set_start_method('spawn')
    # get_context('spawn')
    set_start_method('fork')

    # process = Process(target=worker)
    # process.start()
    # process_2 = Process(target=worker)
    # process_2.start()
    # process.join()
    # process_2.join()
    # que = Queue()
    # for i in range(1, 100):
    #     que.put(i)
    # with Pool(4) as pool:
    #     # results = pool.map(square, que)
    #     results = pool.apply(square, que)
    #     print(results)
    # lock = Lock()
    # for num in range(4):
    #     Process(target=square, args=(num, lock)).start()
    # with Manager() as manager:
    #     shared_list = manager.list()
    #     shared_dict = manager.dict()
    #
    #     processes = []
    #
    #     for i in range(5):
    #         proc = Process(target=worker, args=(i, shared_list, shared_dict))
    #         proc.start()
    #         processes.append(proc)
    #
    #     for proc in processes:
    #         proc.join()
    #
    #     print('Processes finished')
    #     print('Shared list ', list(shared_list))
    #     print('Shared dict ', dict(shared_dict))
    # t1 = time.perf_counter()
    #
    # numbers = list(range(1, 11))
    #
    # with ProcessPoolExecutor(max_workers=2) as executor:
    # # with ThreadPoolExecutor(max_workers=10) as executor:
    #     results = executor.map(compute_sqrt, numbers)
    #     for result in results:
    #         print('Result', result)
    #
    # print('*' * 100)
    # print('Time spent', time.perf_counter() - t1)
    html_pages = [
        "<html><head><title>Python 1</title></head><body></body></html>",
        "<html><head><title>Python 2</title></head><body></body></html>",
        "<html><head><title>Python 3</title></head><body></body></html>",
        "<html><head><title>Python 4</title></head><body></body></html>",
        "<html><head></head><body><h1>No title</h1></body></html>",
    ]
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(extract_title, html) for html in html_pages]
        print(futures)

        for future in as_completed(futures):
            result = future.result()
            print('Result', result)
    #     results = executor.map(extract_title, html_pages)
    #
    # for i, title in enumerate(results, start=1):
    #     print(i, title)

