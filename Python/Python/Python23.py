import threading
import time
from random import randint
'''条件变量锁'''


class Producer(threading.Thread):
    def run(self):
        global L
        while True:
            val = randint(0, 10)