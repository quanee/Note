'''Python继承 多继承'''


class father(object):
    def f1(self):
        print('father.f1')

    def f2(self):
        print('father.f2')


class son(father):
    def f1(self):
        super(son, self).f1()  # 执行父类方法f1
        print('son.f1')

    def f2(self):
        print('son.f2')


s = son()
s.f1()


class mother(object):
    def f1(self):
        print('mother.f1')


# 多继承 按继承顺序查找方法 共同基类最后查找
class s(mother, father):
    pass


s = s()
s.f1()

# ##########################################

