import threading
import time
'''信号量锁'''


class myThread(threading.Thread):
    def run(self):
        if semaphore.acquire():
            print(self.name)
            time.sleep(2)
            semaphore.release()


if __name__ == "__main__":

    semaphore = threading.BoundedSemaphore(5)
    thrs = []

    for i in range(23):
        thrs.append(myThread())