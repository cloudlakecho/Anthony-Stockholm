
# distortion.py
# Cloud Cho December 11, 2018 - Calculate distortion of network
#
# Error:
#
# Comment:
#
# To do:
#   Intrinsic dynamic
#

# Reference:
#   Network instability: https://www.nature.com/articles/srep09450
#   Prediction model: https://machinelearningmastery.com/make-predictions-scikit-learn/
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


def F(X, C):
    # X(t) = {x_1(t), x_2(t), ...}: population of entities
    # f_i(x_i): instrinsic dyanmic
    # F(X) = {f_1(x_1), f_2(x_2)...}: intrinsic dyanamic for whole network

    # To do
    # Mean-Field Description
    # Catastrophic Phase Transitions and Early Warnings in a Spatial Ecological Model
    # Fern´andez and H Fort

    # Coupled phase osillator
    # Synchronization reveals topological scales in complex networks
    # Alex Arenas, Albert D´ıaz-Guilera, and Conrad J. P´erez-Vicente

    period = 32
    z_size = 200
    z = gen(period, z_size)
    x_1 = np.random.randint(len(z), size=period)
    X = [x_1]    
    F = [f_1(x_1)]

# with other nodes—animal or human population
# is a prime example. The combination of the evolving dynamics, the
# peer influence, and the random perturbation leads to a network of
# stochastic differential equations: dX = (F(X,C) - LX)dt + sdW.
def distort(X, C, W, sigma):
    F(X, C) - LX
    sigma
