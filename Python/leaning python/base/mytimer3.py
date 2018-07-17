import time
import sys

"""
Use 3.x keyword-only
"""

trace = lambda *args: None
timefunc = time.clock if sys.platform == 'win32' else time.time


def timer(func, *pargs, _reps=1000, **kargs):
    trace(func, pargs, kargs, _reps)
    start = timefunc()
