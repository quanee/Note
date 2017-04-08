'''yield 模拟协程并发'''


def consumer(name):
    print("starting ...")
    while True:
        new_baozi = yield
        print('[%s] is eating baozi %s' % (name, new_baozi))


def producer():
    con.__next__()
    con2.__next__()
    n = 0
    while n < 5:
        n += 1
        con.send(n)
        con2.send(n)
        print("producer is making baozi %s" % n)


if __name__ == "__main__":
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()