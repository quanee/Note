from pywifi import *
import time
import sys


def scans(face, timeout):
    face.scan()
    time.sleep(timeout)
    return face.scan_results()


def test(i, face, x, key, stu, ts):