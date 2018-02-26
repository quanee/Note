'''
Privacy for attributes fetched from class instances. See self-test code at end of file for a usage example. Decorator same as: Douvler = Private('data', 'size')(Doubler).
Private returns onDecorator, onDecorator returns onInstance, and each onInstance instance embeds a Doubler instance
'''

traceMe = False
def trace(*args):
    if traceMe:
        print('[' + ''.join(map(str, args)) + ']')

def Private(*privates):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)

            def __getattr__(self, attr):
                trace('get:', attr)

                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == 'wrapped':
                    self.__dict__[attr] = value
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)
        return onInstance
    return onDecorator


if __name__ == '__main__':
    traceMe = True

    @Private('data', 'size')
    class Doubler:
        def __init__(self, label, start):
            self.label = label
            self.data = start

        def size(self):
            return len(self.data)

        def double(self):
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
