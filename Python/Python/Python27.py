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

    for i in p_list:
        i.join()
    print('end')
'''
'''
class MyProcess(Process):
    def __init__(self, name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        time.sleep(1)
        print('hello', self.name, time.ctime())


if __name__ == '__main__':
    p_list = []
    for i in range(3):
        p = MyProcess('moonboss')
        p.start()

    for i in p_list:
        i.join()

    print('end')
'''
import os


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('\033[31;1mfunction f\033[0m')
    print('hello', name)


if __name__ == '__main__':
    info('\033[32;1mmain process line\033[0m')
    time.sleep(1)

    p = Process(target=info, args=('bob',))
    p.start()
    p.join()