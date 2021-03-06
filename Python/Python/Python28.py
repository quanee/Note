from multiprocessing import Process, Queue, Pipe
'''进程间通信'''

'''
def f(q, n):
    q.put([42, n, 'hello'])
    print('sub id q', id(q))


if __name__ == '__main__':
    q = Queue()
    print('main id q', id(q))
    p_list = []
    for i in range(3):
        p = Process(target=f, args=(q, i))
        p_list.append(p)
        p.start()
    print(q.get())
    print(q.get())
    print(q.get())

    for i in p_list:
        i.join()
'''

'''
def f(conn):
    conn.send('Hello')
    conn.send([42, None, 'hello'])
    print(conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    print(parent_conn.recv())
    parent_conn.send('hello')
    p.join()
'''
'''
from multiprocessing import Process, Manager


def f(d, l, n):
    d[n] = '1'
    d['2'] = 2
    d[0.25] = None
    l.append(n)
    print(l)


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        li = manager.list(range(5))

        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, li, i))
            p.start()
            p_list.append(p)
        for res in p_list:
            res.join()

        print(d)
        print(li)
'''

from  multiprocessing import Process, Pool
import time


def Foo(i):
    time.sleep(2)
    return i + 100


def Bar(arg):
    print('-->exec done:', arg)

