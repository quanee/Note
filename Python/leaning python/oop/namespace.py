class Super(object):
    def hello(self):
        self.data1 = 'moon'


class sub(Super):
    def hola(self):
        self.data2 = 'boss'



if __name__ == '__main__':
    # 继承树的搜索只发生在引用(object.X),而非赋值(object.X=value)
    print(sub.__dict__)  # 类有自己的命名空间