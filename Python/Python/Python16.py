'''单例模式 永远只有一个实例'''


class Foo(object):
    '''单例模式'''
    __v = None

    @classmethod