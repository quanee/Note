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
        lock.acquire()
        # lockA.acquire()
        print(self.name, "gotlockA", time.ctime())
        lock.release()
        # lockA.release()
        lock.release()
        # lockB.release()

    def run(self):
        self.doA()
        self.doB()


if __name__ == "__main__":

    # lockA = threading.Lock()
    # lockB = threading.Lock()

    lock = threading.RLock()  # 递归锁 可重用(可被多次获取与释放 计数器)
    threads = []