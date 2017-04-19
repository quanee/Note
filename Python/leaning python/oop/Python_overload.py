
'''
常见重载函数(拦截Python内置操作)
__init__    构造函数    对象建立: X = Class(args)
__del__     析构函数    X 对象回收
__add__     运算符 +   如果没有__iadd__ X+Y X+=Y
__or__      运算符|(位or)   如果没有__ior__ X|Y X|=Y
__repr__,__str__    打印转换    print(X) repr(X) str(X)
__call__    函数调用    X(*args, **kargs)
__getattr__ 点号运算符   X.undefined
__setattr__ 属性赋值语句  X.any = value
__delattr__ 属性删除    del X.any
__getattribute__    属性获取    X.any
__getitem__ 索引 分片 迭代    X[key] X[i:j] 没__iter__时的分片 for循环和其他迭代器
__setitem__ 索引和分片赋值 X[key] = value X[i:j] = sequence
__delitem__ 索引和分片删除 del X[key] del X[i:j]
__len__     长度  len(X)如果没有__bool__ 真值测试
__bool__    布尔测试    bool(X) 真值测试(在Python2.6中叫__nonzero__)
__lt__ __gt__   特定的比较   X < Y X > Y X <= Y X >= Y X == Y X != Y (在Python2.6中只有__cmp__)
__le__ __ge__
__eq__ __ne__
__radd__    右侧加法    Other + X
__iadd__    实地(增强的)加法   X+=Y(or else __add__)
__iter__ __next__   迭代环境    l=iter(X),next(l);for loops, in if no __contains__, all comparehensions, map(F, X), others(__next__在Py2.6中称为next)
__contains__    成员关系测试  item in X(任何可迭代)
__index__   整数值 hex(X),bin(X),oct(X),O[X],O[X:](Python2为__oct__,__hex__)
__enter__ __exit__  环境管理器   with obj as var:
__get__ __set__ __delete__  描述符属性   X.attr, X.attr=value,del X.attr
__new__ 创建  在__init__之前创建对象
'''