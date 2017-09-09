#!/usr/bin/env python
# coding=utf-8
from multiprocessing import Process
from multiprocessing import Pool
import os
import time
import random

# Only works on Unix/Linux/Mac:
print('Process (%s) start...' % os.getpid())