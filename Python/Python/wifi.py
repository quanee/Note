from pywifi import *
import time
import sys


def scans(face, timeout):
    face.scan()
    time.sleep(timeout)
    return face.scan_results()