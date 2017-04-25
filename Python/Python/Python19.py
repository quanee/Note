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


def movie(func):
    for i in range(2):
        print("Begin watching at the %s! %s" % (func, ctime()))
        sleep(5)
        print("end watching %s" % ctime())


threads = []
t1 = threading.Thread(target=music, args=('七里香',))
threads.append(t1)
t2 = threading.Thread(target=movie, args=('阿甘正传',))
threads.append(t2)



if __name__ == '__main__':