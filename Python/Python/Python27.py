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