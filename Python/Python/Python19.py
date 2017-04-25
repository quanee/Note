from time import ctime, sleep
import threading
'''
线程实例
计算密集型  c
IO密集型  多线程
'''


def music(func):
    for i in range(2):
        print("Begin listening to %s. %s" % (func, ctime()))
        sleep(1)
        print("end listening %s" % ctime())

