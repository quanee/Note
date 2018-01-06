from multiprocessing import Process, Queue, Pipe
'''进程间通信'''

'''
def f(q, n):
    q.put([42, n, 'hello'])
    print('sub id q', id(q))