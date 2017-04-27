from multiprocessing import Process
import time
'''类式调用'''
'''
def f(name):
    time.sleep(1)
    print('hello', name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = Process(target=f, args=('moonboss',))
        p_list.append(p)
        p.start()
