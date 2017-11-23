
def classtree(cls, indent):
    print('.' * indent + cls.__name__)

    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)

def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def selftest():
    class A:
        ...


    class B(A):
        ...


    class C(A):
        ...


    class D(B, C):
        ...


    class E:
        ...

