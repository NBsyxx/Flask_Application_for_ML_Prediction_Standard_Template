
import gc
import os

import numpy as np
import pandas as pd

from sklearn.metrics import mean_squared_error
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import median_absolute_error


from scipy.stats import randint as sp_randint 
from scipy.stats import uniform as sp_unif


from xgboost import XGBRegressor
from xgboost import XGBClassifier
from xgboost import plot_tree

import matplotlib.pyplot as plt
import seaborn as sns
import joblib

def reduce_mem_usage(df, verbose=True):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    start_mem = df.memory_usage().sum() / 1024**2    
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)    
    end_mem = df.memory_usage().sum() / 1024**2
    if verbose: print('Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)'.format(end_mem, 100 * (start_mem - end_mem) / start_mem))
    return df

def main():
    df = pd.read_csv("train_test.csv")

    features = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6']
    X = df[features]
    y = df['target']

    # copy and paste feature engineering code here.

    seed = 10
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, test_size=0.2, random_state = seed)

    xgb = XGBRegressor(seed=seed,silent=1)

    xgb = XGBRegressor(
            seed             = 0,
            silent           = 1,
            learning_rate    = 0.1, 
            n_estimators     = 568,
            max_depth        =  2,
            gamma            = 1,
            subsample        = 0.8,
            colsample_bytree = 0.8,
            verbose = 101
        ).fit(X_train, y_train)
    joblib.dump(xgb,"model.joblib")

main()