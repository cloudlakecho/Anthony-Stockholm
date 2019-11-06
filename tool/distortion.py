
# distortion.py
# Cloud Cho December 11, 2018 - Calculate distortion of network
#
# Error:
#
# Comment:
#
# To do:
#   Intrinsic dynamic
#   gen function

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
import pdb

from pathlib2 import Path #  pipy library
from inspect import currentframe, getframeinfo
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten, Conv2D


def gen(period, z_size):

    return z

def F(X, C):
    n = 2
    m = 3
    k = 4

    # X(t) = {x_1(t), x_2(t), ...}: population of entities
    # f_i(x_i): instrinsic dyanmic
    # F(X) = {f_1(x_1), f_2(x_2)...}: intrinsic dyanamic for whole network

    # To do
    # (1) Mean-Field Description
    # Catastrophic Phase Transitions and Early Warnings in a Spatial Ecological Model
    # Fern´andez and H Fort

    # (2) Coupled phase osillator
    # Synchronization reveals topological scales in complex networks
    # Alex Arenas, Albert D´ıaz-Guilera, and Conrad J. P´erez-Vicente

    # Idea
    # x_i(t) could 1 by n array, which is n vector
    # ex) 32 t^7 + 34 t^5 + 0.25 t^2 + 10 + 40 / t
    # f_i(x_i) coud be 1 by m array as well like
    # 32 x_i^7 + 34 x_i^5 + 0.25 x_i^2 + 10 + 40 / x_i
    # The desgin could set what is dimension and then iteration find the
    # best constant group.

    t = np.ones((m, 1))  # m by 1
    c_x = np.ones((n, m))
    X = np.dot(c_x, t)  # n by 1

    c_f = np.ones((k, n))
    F = np.dot(c_f, X)  # k by 1 - Reveiw required

    # -----
    period = 32
    z_size = 200

    # To do
    z = gen(period, z_size)

    x_1 = np.random.randint(len(z), size=period)
    X = [x_1]
    print(X)
    F = lambda X: X + np.random()

    pdb.set_trace()

    print(F)

    return F

# with other nodes—animal or human population
# is a prime example. The combination of the evolving dynamics, the
# peer influence, and the random perturbation leads to a network of
# stochastic differential equations: dX = (F(X,C) - LX)dt + sdW.
def distort(X, C, W, sigma):
    X = 0
    C = 0
    LX = 0
    print(F(X, C) - LX)
    sigma
