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

