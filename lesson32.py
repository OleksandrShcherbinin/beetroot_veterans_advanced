import queue
import time
import threading
from concurrent.futures import ThreadPoolExecutor


def worker_1(name: str, que: queue.Queue) -> None:
    print(f'Hello {name}! Working in thread {que.get()}')
    time.sleep(3)
    print(f'Bye {name}! Function finished in thread')


def worker_2(name: str, que: queue.Queue) -> None:
    print(f'Hello {name}! Working in thread {que.get()}')
    time.sleep(3)
    print(f'Bye {name}! Function finished in thread')


def worker_3(name: str, que: queue.Queue) -> None:
    print(f'Hello {name}! Working in thread {que.get()}')
    time.sleep(3)
    print(f'Bye {name}! Function finished in thread')


class BankAccount:
    def __init__(self):
        self.balance = 100
        self.lock = threading.Lock()

    def update(self, transaction: str, amount: int):
        print(f'{transaction} transaction updating...')
        with self.lock:
            balance_copy = self.balance
            if transaction == 'deposit':
                balance_copy += amount
            if transaction == 'withdraw':
                balance_copy -= amount
            time.sleep(1)
            self.balance = balance_copy
        print(transaction, 'finishing...')


# semaphore = threading.Semaphore(3)
semaphore = threading.BoundedSemaphore(3)


def access_api(thread_id):
    print(thread_id, 'Waiting for response')
    with semaphore:
        print(thread_id, 'Got access')
        time.sleep(2)
        print(thread_id, 'Finished access')


def access_db(thread_id):
    try:
        semaphore.acquire()
        print(thread_id, 'Working')
        time.sleep(1)
    except Exception as e:
        print(e)
    finally:
        semaphore.release()


if __name__ == '__main__':
    q = queue.Queue()
    # for i in range(1, 11):
    #     q.put(i)
    # t_1 = threading.Thread(target=worker_1, args=('Inna', q))
    # t_1.start()
    # t_2 = threading.Thread(target=worker_2, args=('Roman', q))
    # t_2.start()
    # t_3 = threading.Thread(target=worker_3, args=('Borys', q))
    # t_3.start()
    # t_1.join()
    # t_2.join()
    # t_3.join()
    # print('Main thread start')
    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     for name in ('Inna', 'Roman', 'Borys'):
    #         executor.submit(worker_1, name, q)
    # print('Main thread finished')
    # account = BankAccount()
    # print('Bank account', account.balance)
    #
    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     for transaction, amount in [('deposit', 50), ('withdraw', 50)]:
    #         executor.submit(account.update, transaction, amount)
    #
    # print('Finished bank account update', account.balance)
    # for i in range(6):
    #     threading.Thread(target=access_db, args=(i,)).start()
    new_event = threading.Event()
    orders = []


    # def producer():
    #     time.sleep(2)
    #     orders.append('Order #1')
    #     new_event.set()
    condition = threading.Condition()


    def producer():
        for i in range(3):
            time.sleep(1)
            with condition:
                orders.append('Order #1')
                condition.notify()


    # def consumer():
    #     print('Waiting for order')
    #     new_event.wait()
    #     print(f'Working on order {orders.pop()}')

    def consumer():
        while True:
            with condition:
                while not orders:
                    condition.wait()
                order = orders.pop()
                print('Working on order', order)


    # threading.Thread(target=consumer, daemon=True).start()
    # threading.Thread(target=producer).start()


    def delayed():
        print('After 1.5 seconds')
        print(threading.current_thread().name)
        print(threading.get_ident())

    threading.Timer(1.5, delayed).start()

    print(threading.active_count())
    print(threading.current_thread().name)
    print(threading.enumerate())
