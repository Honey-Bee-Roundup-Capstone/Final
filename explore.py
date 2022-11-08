# Basic Data Science Imports
import pandas as pd
import numpy as np
import os
import wrangle
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()

# Stats and M odeling imports
from scipy import stats
from math import sqrt
import regression_models as model
from sklearn.preprocessing import MinMaxScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,explained_variance_score, r2_score
from sklearn.linear_model import LinearRegression,LassoLars,TweedieRegressor
from sklearn.feature_selection import SelectKBest, RFE, f_regression
from sklearn.model_selection import train_test_split
import sklearn.preprocessing



def split_data(df):
    '''This function takes in a dataframe and returns three dataframes, a training dataframe with 60 percent 
        of the data, a validate dataframe with 20 percent of the data and test dataframe with 20 percent of the data.'''
    # split data into train and test with a test size of 20 percent and random state of 825
    train, test = train_test_split(df, test_size=.2, random_state=825)
    # split train again into train and validate with a validate size of 25 percent of train
    train, validate = train_test_split(train, test_size=.25, random_state=825)
    # return three dataframes, 60/20/20 split
    return train, validate, test


# plot to visualize actual vs predicted. 
def model_performace(y_validate):
    """This function will take in y validate and output model perforamce visualization"""
    #set figure size
    plt.figure(figsize=(16,8))
    #histogram distribution of target
    plt.hist(y_validate.colonies_lost, color='blue', alpha=.5, label="Actual colony lost")
    #histogram distribution of target predicted by linear regression model
    plt.hist(y_validate.colonies_lost_pred_lm, color='red', alpha=.5, label="Model: LinearRegression")
    #histogram distribution of target predicted by Tweedie regressor model
    plt.hist(y_validate.colonies_lost_pred_glm, color='yellow', alpha=.5, label="Model: TweedieRegressor")
    #histogram distribution of target predicted by LassoLars model
    plt.hist(y_validate.colonies_lost_pred_lars, color='green', alpha=.5, label="Model:Lassolars")
    #histogram distribution of target predicted by Polynomial model
    plt.hist(y_validate.colonies_lost_pred_lm2, color="cyan", alpha=.5, label="Model 2nd degree Polynomial")
    plt.xlabel("colony lost")
    plt.ylabel("count")
    plt.title("Comparing the distribution of actual colony lost to predicted distributions for the top models")
    plt.legend()
    plt.show()
