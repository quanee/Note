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
        # lockB.acquire()
        print(self.name, "gotlockB", time.ctime())
        lock.release()
        # lockB.release()
        lock.release()
        # lockA.release()

    def doB(self):
        lock.acquire()
        # lockB.acquire()
        print(self.name, "gotlockB", time.ctime())
        time.sleep(2)