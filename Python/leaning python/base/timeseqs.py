import sys
import mytimer

reps = 10000
repslist = range(reps)


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

