"""
boids.py 

Implementation of Craig Reynold's BOIDs

Author: Mahesh Venkitachalam
"""

import sys, argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.spatial.distance import squareform, pdist, cdist
from numpy.linalg import norm

width, height = 640, 480


class Boids():
    def __init__(self):
        self.angles = 2 * math.pi * np.random.rand(N)
        self.N = N
        self.pos = [width / 2.0, height / 2.0] + np.random(2, N).reshape(N, 2)
        self.vel = np.array(list(zip(np.sin(angles), np.cos(angles))))
        self.minDist = 25.0
        self.maxRuleVel = 0.03
        self.maxVel = 2.0

    def tick(self, frameNum, pts, beak):
        self.distMatrix = squareform(pdist(self.pos))
        self.vel += self.applyRules()
        self.limit(self.vel, self.maxVel)
        self.pos += self.vel
        self.applyBC()
        pts.set_data(self.pos, self.distMatrix)
