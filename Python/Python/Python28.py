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