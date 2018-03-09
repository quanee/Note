import threading
import time
'''死锁和递归锁'''


class myThread(threading.Thread):
    def doA(self):
        lock.acquire()
        # lockA.acquire()
        print(self.name, "gotlockA", time.ctime())
        time.sleep(3)
        lock.acquire()