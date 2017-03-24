from classtools import AttrDisplay

'''
实例创建      填充实例属性
行为方法      在类方法中封装逻辑
运算符重载    为打印这样的操作提供行为
定制行为      重新定义子类中的方法以使其特殊化
定制构造函数  为超类步骤添加初始化逻辑
'''

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]
