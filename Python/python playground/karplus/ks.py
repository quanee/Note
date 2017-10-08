import sys
import os
import time
import random
import wave
import argparse
import pygame
import numpy as np
from collections import deque
from matplotlib import pyplot as plt

# show plot of algorithm in action?
gShowPlot = False

# notes of a Pentatonic Minor scale
# piano C4-E(b)-F-G-B(b)-C5
pmNotes = {'C4': 262, 'Eb': 311, 'F': 349, 'G': 391, 'Bb': 466}

# write out WAV file


def writeWAVE(fname, data):
    # open file
    file = wave.open(fname, 'wb')