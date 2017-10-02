class Super(object):
    def hello(self):
        self.data1 = 'moon'


class sub(Super):
    def hola(self):
        self.data2 = 'boss'



if __name__ == '__main__':
    # 继承树的搜索只发生在引用(object.X),而非赋值(object.X=value)
    print(sub.__dict__)  # 类有自己的命名空间

    X = sub()
    print(X.__dict__)  # 实例命名空间初始为空

    X.hola()
    print(X.__dict__)  # 属性位于实例的属性命名空间字典内 随实例的不同而不同 self正是进入其命名空间的钩子

    X.hello()
    print(X.__dict__)
    # {'data2': 'boss', 'data1': 'moon'}
    print(X.__dict__.keys())
    # dict_keys(['data2', 'data1'])
    print(dir(X))
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'data1', 'data2', 'hello', 'hola']