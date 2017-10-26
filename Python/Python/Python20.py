import threading
import time
'''共享锁'''

r = threading.Lock()


def addNum():
    global num

    #  安全 线程切换时无操作
    # num -= 1

    r.acquire()  # 获取锁