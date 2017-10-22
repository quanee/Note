'''组合类 委托实现'''

class Person(object):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager():
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)


    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)


    def __getarr__(self, attr):
        return getattr(self.person, attr)


    def __str__(self):
        return str(self.person)



if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)

    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    # print(tom.lastName())
    print(tom)

    # 内省工具
    print(bob.__class__)
    print(bob.__class__.__name__)
    print(list(bob.__dict__.keys()))
    for key in bob.__dict__:
        print(key, '=>', bob.__dict__[key])