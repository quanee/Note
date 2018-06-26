class Bad(Exception):
    ...


def doomed():
    raise Bad()

