import threading
import time
'''共享锁'''

r = threading.Lock()


def addNum():
    global num

    #  安全 线程切换时无操作
    # num -= 1

    r.acquire()  # 获取锁
    # 线程不安全
    temp = num
    time.sleep(0.001)
    print('ok')