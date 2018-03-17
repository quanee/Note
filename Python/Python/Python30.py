import greenlet
'''greenlet 协程


def test1():
    print(12)
    gr2.switch()
    print(56)
    gr2.switch()


def test2():
    print(34)
    gr1.switch()
    print(78)


gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
gr1.switch()
'''

'''gevent 协程

import gevent
import time


def foo():
    print('Running in foo', time.ctime())
    gevent.sleep(1)
    print('Explicit context switch to foo again', time.ctime())


def bar():
    print('Running in bar', time.ctime())
    gevent.sleep(1)
    print('Explicit context switch to bar again', time.ctime())


gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar),
    # gevent.spawn(func),
])'''

from gevent import monkey
monkey.patch_all()  # Windows IO阻塞监听补丁
import gevent
from urllib.request import urlopen


def f(url):
    print('GET: %s' % url)
    resp = urlopen(url)
    data = resp.read()