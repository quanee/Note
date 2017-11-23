
def classtree(cls, indent):
    print('.' * indent + cls.__name__)

    for supercls in cls.__bases__:
        classtree(supercls, indent + 3)

def instancetree(inst):