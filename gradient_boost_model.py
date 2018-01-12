#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:42:06 2017

@author: dyinanc
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('kc_house_data.csv')
current=0
selected_columns=[]
for column in dataset.columns.values:
    if(current in list(range(3,5)) +list(range(7,8))+ list(range(12,15)) + list(range(16,17)) +list(range(19,21))):
        selected_columns.append(column)
    current+=1
X = dataset.iloc[:, list(range(3,5)) +list(range(7,8))+ list(range(12,15)) + list(range(16,17)) +list(range(19,21))].values
y = dataset.iloc[:, 2].values

# HotEncode Zipcodes
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [6])
X = onehotencoder.fit_transform(X).toarray()

# Avoid dummy variable trap
X = X[:,1:]

# Model split into training and test
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn import ensemble
regressor = ensemble.GradientBoostingRegressor(n_estimators = 400, max_depth = 5, min_samples_split = 2,
          learning_rate = 0.1, loss = 'ls')

regressor.fit(X_train, y_train)
regressor.score(X_test, y_test)

y_pred = regressor.predict(X_test)

import pickle

pickle.dump( regressor, open( "gradient_boost_model.p", "wb" ) )
pickle.dump(onehotencoder,open( "gradient_boost_model_onehotencoder.p", "wb" ) )