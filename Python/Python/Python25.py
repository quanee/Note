import queue


'''
q.qsize() 返回队列的大小
q.empty() 如果队列为空，返回True,反之False
q.full() 如果队列满了，返回True,反之False
q.full 与 maxsize 大小对应
q.get([block[, timeout]]) 获取队列，timeout等待时间
q.get_nowait() 相当q.get(False)
非阻塞 q.put(item) 写入队列，timeout等待时间
q.put_nowait(item) 相当q.put(item, False)
q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
q.join() 实际上意味着等到队列为空，再执行别的操作'''

d = queue.Queue(3)  # 参数小于0 无限大

d.put('a', 0)
d.put('b')
d.put('c')
# d.put('c', 0)  # 队列满时 阻塞 参数0 报错

print(d.get())
print(d.get())
print(d.get())
# print(d.get(0))  # 队列空时 阻塞 参数0 报错

import threading
import time


li = [1, 2, 3, 4, 5]


def pri():
    while li:
        a = li[-1]
        print(a)
        time.sleep(1)
        try:
            li.remove(a)
        except Exception:
            print('----', a)


t1 = threading.Thread(target=pri, args=())
t1.start()
t2 = threading.Thread(target=pri, args=())
t2.start()


import random


class Production(threading.Thread):
    def run(self):
        while True:
            r = random.randint(0, 100)
            q.put(r)
            print("生产出来%s号包子" % r)