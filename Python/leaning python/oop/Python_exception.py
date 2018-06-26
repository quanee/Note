class Bad(Exception):
    ...


def doomed():
    raise Bad()


try:
    doomed()
except Bad:
    print('got Bad')

