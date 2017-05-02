'''
Class decorate with Private and Public attribute declarations.
Controls access to attrivutes stroed on an instance, or inherited
by it from its classes. Private declares attribute names that connot be fetched or assigned outside the decorated class, and Public declares all the names that can. Caveat: this works in for normally named attributes only: __X__ operator overloading methods implicitly run for built-in operations do not trigger either __getattr__ or __getattribute__ in new-style classesl.
Add __X__ methods here to intercept and delegate built-ins
'''

traceMe = False
def trace(*args):
    if traceMe:
        print('[' + ''.join(map(str, args)) + ']')


def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)