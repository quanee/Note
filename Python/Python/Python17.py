import threading
import time

begin = time.time()


def foo(n):
    print('foo%s' % n)
    time.sleep(1)
    print('end foo')


def bar(n):
    print('bar%s' % n)
    time.sleep(2)