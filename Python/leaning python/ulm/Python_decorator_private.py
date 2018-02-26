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