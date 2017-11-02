# Regression Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('kc_house_data.csv')
X = dataset.iloc[:, list(range(3,4)) +list(range(7,12))+ list(range(12,15)) + list(range(16,17)) +list(range(19,21))].values
y = dataset.iloc[:, 2].values

# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 8] = labelencoder_X.fit_transform(X[:, 9])
onehotencoder = OneHotEncoder(categorical_features = [9])
X = onehotencoder.fit_transform(X).toarray()


# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Avoid dummy variable trap
X = X[:,1:]

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
import statsmodels.formula.api as sm
X_train = np.append(arr=np.ones((len(X_train),1)).astype(int),values=X_train,axis=1)
X_opt = X_train[:,list(range(0,80))]
regressor_OLS = sm.OLS(endog=y_train,exog=X_opt).fit()
regressor_OLS.summary()