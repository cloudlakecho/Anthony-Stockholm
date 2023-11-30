
# main.py in Anthony-Stockholm
# Cloud Cho May 26, 2018 - Perfomr Pricipal Component Analysis, PCA
#
# (1) Catastropy prediction
# (2) Smaller company stock price prediction
#
# Input:
#
# Output:
#
# Error:
#   error exist
#   Matrix shape
#
# Comment:
#

import numpy as np
import sklearn
from sklearn.decomposition import PCA

import argparse, sys
import keras
import os.path
import pdb  # Debugging
import random

# from pathlib2 import Path #  pipy library
from inspect import currentframe, getframeinfo
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten, Conv2D
from keras.utils import np_utils
from tool import distortion, pca, lstm


def main():
    if (sys.argv[1] == '1'):
        catastropy_predict()
    elif (sys.argv[1] == '2'):
        smaller_company_predict()
    elif (sys.argv[1] == '3'):
        investor_predict()


def catastropy_predict():
    col = 2
    row = 3
    X = np.random.normal(0, 0.33, size=[row, col]).astype(np.float32)
    C = random.randint(0, 100)
    print(X)
    pca.pca(X)
    distortion.F(X, C)


def smaller_company_predict():
    company = 500
    period = 365000
    features = 1
    sp_history = np.zeros((company, period))
    dataY = np.zeros(company)

    # Error
    # Matrix shape
    # reshape to be [samples, time steps, features]
    X = np.reshape(sp_history, (company, period, features))
    y = np_utils.to_categorical(dataY)

    lstm.train_model(X, y)


# To check investor prediction with specific stretegy and find unusual year
#    Any firm or strategy perform differently in unsual year?   
def investor_predict():    
    investor_name = "Berkshire Hathaway"
    no_year = 100
    strageg_name = "Sell in May and go away"
    selected_investor = Investor_Record(name=investor_name)
    selected_stock = selected_investor.stock(percentage=no_year)
    selected_strategy = Strategy(name=strategy_name)  
    strategy_output = dict()                             
    for idx, stock in enumerate(selected_stock):
        #
        # To do
        # Go through many years depending on percentage
        #
        buy_cost = selectred_stragy.cost(item=stock)
        sel_cost = selectred_stragy.cost(item=stock)
        change = sel_cost - buy_cost
        strtegy_output[stock] = change 
        

        


if __name__ == '__main__':
    print(sklearn.__version__)
    main()
