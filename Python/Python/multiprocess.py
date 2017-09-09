#!/usr/bin/env python
# coding=utf-8
from multiprocessing import Process
from multiprocessing import Pool
import os
import time
import random

# Only works on Unix/Linux/Mac:
print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# multiprocessing模块调用
""" 子进程要执行的代码"""


def run_proc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))
    if __name__ == '__main__':
        print('Parent process %s.' % os.getpid())
        p = Process(target=run_proc, args=('test_code',))
        print('Child process will start.')
        p.start()
        p.join()
        print('Child process end.')


# 进程池 Pool
# 如果要启动大量的子进程，用进程池的方式批量创建子进程：
def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("Task %s run %0.f seconds." % (name, (end - start)))
    if __name__ == "__main__":
        print("Parent process %s." % os.getpid())
        p = Pool(4)
        for i in range(5):
            p.apply_async(long_time_task, args=(i,))
            print("Waiting for all subprocess done...")
            p.close()
            p.join()
            print("All subprocess done.")

'''
对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，
调用close()之后就不能继续添加新的Process了。

注意输出的结果，task0，1，2，3是立刻执行的，而task4要等待前面某个task完成后才执行，
这是因为Pool的默认大小设置成了4(p = Pool(4))，代表着最多同时执行4个进程。
这是Pool有意设计的限制，并不是操作系统的限制。如果改成:
p = Pool(5)
就可以跑5个进程了。
由于Pool的默认大小是CPU的核数，如果你拥有8核CPU，提交至少9个子进程才能看到上面的等待效果。
子进程