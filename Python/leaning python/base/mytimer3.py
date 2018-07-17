import time
import sys

"""
Use 3.x keyword-only
"""

trace = lambda *args: None
timefunc = time.clock if sys.platform == 'win32' else time.time