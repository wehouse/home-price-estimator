class KingCountyModels:      
    def create_regressor(self):    
        import numpy as np
        import matplotlib.pyplot as plt
        import pandas as pd
        
        dataset = pd.read_csv('kc_house_data.csv')
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
        from sklearn.linear_model import LinearRegression
        regressor = LinearRegression()
        regressor.fit(X_train, y_train)
        
        return regressor, onehotencoder