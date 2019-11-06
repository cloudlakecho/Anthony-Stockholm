
# main.py in Anthony-Stockholm
# Cloud Cho May 26, 2018 - Perfomr Pricipal Component Analysis, PCA
#
# Input:
#
# Output:
#
# Error:
#   error exist
#
# Comment:
#

import numpy as np
import sklearn
from sklearn.decomposition import PCA

import argparse
import keras
import os.path
import pdb  # Debugging
import random

# from pathlib2 import Path #  pipy library
from inspect import currentframe, getframeinfo
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten, Conv2D
from tool import distortion, pca


def main():
    col = 2
    row = 3
    X = np.random.normal(0, 0.33, size=[row, col]).astype(np.float32)
    C = random.randint(0, 100)
    print(X)
    pca.pca(X)
    distortion.F(X, C)


if __name__ == '__main__':
    print(sklearn.__version__)
    main()
