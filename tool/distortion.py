
# distortion.py
# Cloud Cho December 11, 2018 - Calculate distortion of network
#
# Error:
# 
# Comment:
# 
# Reference: 
#   https://www.nature.com/articles/srep09450
#

import numpy as np
import sklearn
from sklearn.decomposition import PCA

import argparse
import keras
import os.path

from pathlib2 import Path #  pipy library
from inspect import currentframe, getframeinfo
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten, Conv2D


# with other nodes—animal or human population
# is a prime example. The combination of the evolving dynamics, the
# peer influence, and the random perturbation leads to a network of
# stochastic differential equations: dX = (F(X,C) - LX)dt 1 sdW.
def distort(X, C, W, sigma):
    pass
