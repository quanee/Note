import sys
import argparse
import math
import numpy as np
import matplotlib.pylab as plt
import matplotlib.animation as animation
from scipy.spatial.distance import squareform
from scipy.spatial.distance import pdist
from scipy.spatial.distance import cdist
from numpy.linalg import norm
"""模拟鸟群"""



width, height = 1000, 1000


class Boids:
    """class that represents Boids simulation"""

    def __init__(self, N):
        """initialize the Boid simulation"""
        self.pos = [width / 2.0, height / 2.0] + 10 * np.random.rand(2 * N).reshape(N, 2)
        # normalized random velocaties
        angles = 2 * math.pi * np.random.rand(N)
        self.vel = np.array(list(zip(np.sin(angles), np.cos(angles))))
        self.N = N
        # minimum destance of approach
        self.minDist = 25.0
        # minimum magnitude of velocities calculated by "rules"
        self.maxRuleVel = 0.03
        # maximum maginit of the final velocity
        self.maxVel = 2.0

    def tick(self, frameNum, pts, beak):
        """Update the simulation by one time step."""
        # get pairWise distances
        self.distMatrix = squareform(pdist(self.pos))
        # apply rules:
        self.vel += self.applyRules()
        self.limit(self.vel, self.maxVel)
        self.pos += self.vel
        self.applyBC()
        # update data
        pts.set_data(self.pos.reshape(2 * self.N)[::2], self.pos.reshape(2 * self.N)[1::2])
        vec = self.pos + 10 * self.vel / self.maxVel
        beak.set_data(vec.reshape(2 * self.N)[::2], vec.reshape(2 * self.N)[1::2])

    def limitVec(self, vec, maxVal):
        """limit the magnitide of the 2D vector"""
        mag = norm(vec)