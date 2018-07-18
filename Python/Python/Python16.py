'''单例模式 永远只有一个实例'''


class Foo(object):
    '''单例模式'''
    __v = None

    @classmethod
    def get_instance(cls):
        if not cls.__v:
            cls.__v = Foo()

        return cls.__v


obj1 = Foo.get_instance()
print(obj1)
obj2 = Foo.get_instance()
print(obj1)
obj3 = Foo.get_instance()
print(obj1)

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        import time
        self.write(str(time.time()))


application = tornado.web.Application([
    (r'/index', MainHandler),
])

if __name__ == '__mian__':