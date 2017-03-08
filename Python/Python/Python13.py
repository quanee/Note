'''metaclass元类'''


class MyType(type):
    def __init__(self, *args, **kwargs):
        print(123)

    def __call__(self, *args, **kwargs):  # 2