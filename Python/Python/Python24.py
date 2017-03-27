import threading
import time


'''
同步条件(事件)
event.isSet()：返回event的状态值；
event.wait()：如果 event.isSet()==False将阻塞线程 默认False
event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
event.clear()：恢复event的状态值为False。
'''


class Boss(threading.Thread):
    def run(self):
        print("BOSS：今晚大家都要加班到22:00。")
        event.isSet() or event.set()
        time.sleep(5)
        print("BOSS：<22:00>可以下班了。")
        event.isSet() or event.set()


class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker：哎……命苦啊！")
        time.sleep(0.25)
        event.clear()
        event.wait()
        print("Worker：Oh Yeah!")


if __name__ == "__main__":
    event = threading.Event()
    threads = []
