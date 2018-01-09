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