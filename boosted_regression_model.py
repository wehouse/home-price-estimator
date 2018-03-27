# -*- coding: utf-8 -*-

from sklearn import ensemble
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle


data = pd.read_csv('kc_house_data.csv')
labels = data.price
conv_dates = [1 if values==2014 else 0 for values in data.date]
data.date =conv_dates
dataset = data.drop(['id', 'price'],axis=1)

# Model split into training and test
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(dataset, labels, test_size = 0.1, random_state = 2)

clf = ensemble.GradientBoostingRegressor(n_estimators = 400, max_depth=5, min_samples_split=2, learning_rate = 0.1, loss='ls')

clf.fit(X_train, y_train)

clf.score(X_test,y_test)

# Dump regressor to pickle file for future use
pickle.dump( clf, open( "boosted_regression.p", "wb" ) )

# Plotting number of estimators vs loss function
t_sc = np.zeros((400),dtype=np.float64)
y_pred = clf.predict(X_test)
for i,y_pred in enumerate(clf.staged_predict(X_test)):
    t_sc[i]=clf.loss_(y_test,y_pred)
    
testsc = np.arange((400))+1

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(testsc,clf.train_score_,'b-',label= 'Set dev train')
plt.plot(testsc,t_sc,'r-',label = 'set dev test')


# Try a new input value
zipcode=98002
bedrooms=3
bathrooms=2.5
floors=2
sqft_above=2000
sqft_basement=800
year_built=2010
sqft_living=2100
sqft_lot=2600
date=2015
waterfront=0
view=0
condition=3
grade=8
year_renovated=0
zipcode=98117
lat=47.6849
long=-122.376
sqft_living15=1360
sqft_lot=5074

# date is 0 or 1 if 2014
date = 0

input_arr= []
input_arr = np.append(input_arr, date)
input_arr = np.append(input_arr, bedrooms)
input_arr = np.append(input_arr, bathrooms)
input_arr = np.append(input_arr, sqft_living)
input_arr = np.append(input_arr, sqft_lot)
input_arr = np.append(input_arr, floors)
input_arr = np.append(input_arr, waterfront)
input_arr = np.append(input_arr, view)
input_arr = np.append(input_arr, condition)
input_arr = np.append(input_arr, grade)

input_arr = np.append(input_arr, sqft_above)
input_arr = np.append(input_arr, sqft_basement)
input_arr = np.append(input_arr, year_built)
input_arr = np.append(input_arr, year_renovated)
input_arr = np.append(input_arr, zipcode)
input_arr = np.append(input_arr, lat)
input_arr = np.append(input_arr, long)
input_arr = np.append(input_arr, sqft_living15)
input_arr = np.append(input_arr, sqft_lot)

print(clf.predict([input_arr]))