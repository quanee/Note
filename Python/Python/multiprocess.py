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
