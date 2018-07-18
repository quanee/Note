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