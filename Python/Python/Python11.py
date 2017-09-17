'''字段 属性 属性方法'''



class Foo(object):
    static_var = '静态字段'

    def __init__(self):
        self.name = '普通字段'

    def func(self):
        print("普通方法 对象调用")

    @staticmethod
    def sta():
        print("静态方法 类直接调用")

    @classmethod
    def clsf(cls):
        print("当前类", cls)