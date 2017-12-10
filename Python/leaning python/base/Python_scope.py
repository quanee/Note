
'''作用域'''

# 作用域搜索顺序
# L(Local) function 本地作用域
# E(Enclosing) function locals 上层作用域
# G(Global) module 全局作用域
# B(Built-in) Python 内置作用域



x = 1


def scp():
    print(x)

    # x = 1  # UnboundLocalError: local variable 'x' referenced before assignment


scp()


# 内置作用域
import builtins

print(dir(builtins))
