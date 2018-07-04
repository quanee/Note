import threading
import time
'''信号量锁'''


class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():