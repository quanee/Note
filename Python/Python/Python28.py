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
