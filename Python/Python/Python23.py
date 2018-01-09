import threading
import time
from random import randint
'''条件变量锁'''


class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val = randint(0, 10)
            print('生产者', self.name, ":Append" + str(val), L)
            if lock_con.acquire():
                L.append(val)
                lock_con.notify()
                lock_con.release()
            time.sleep(1)


class Consumer(threading.Thread):
    def run(self):
        global L
        while True:
                lock_con.acquire()
                if len(L) == 0:
                    lock_con.wait()
                print('消费者', self.name, ":Delete" + str(L[0]), L)
                del L[0]
                lock_con.release()
                time.sleep(0.25)


if __name__ == "__main__":

    L = []
    lock_con = threading.Condition()
    threads = []
    for i in range(5):
        threads.append(Producer())
    threads.append(Consumer())

    for t in threads:
        t.start()
