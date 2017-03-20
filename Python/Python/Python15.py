'''反射'''


class Foo(object):
    def __init__(self, name):
        self.name = name

    def show(self):
        return self.name


b = 'name'
obj = Foo('moon')
name = obj.__dict__[b]