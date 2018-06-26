class Bad(Exception):
    ...


def doomed():
    raise Bad()


try:
    doomed()
except Bad:
    print('got Bad')


'''
try:
    ...
except:
    ...
else:
    try语句没有引发异常时执行
'''