'''yield 模拟协程并发'''


def consumer(name):
    print("starting ...")
    while True:
        new_baozi = yield
        print('[%s] is eating baozi %s' % (name, new_baozi))

