#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:25:57 2017

@author: dyinanc
"""
import pandas as pd
import numpy as np
import pickle

from linear_model import KingCountyLinearModel
dataset = pd.read_csv('kc_house_data.csv')

kingC = KingCountyLinearModel()
regressor,onehotencoder= kingC.create_regressor()

pickle.dump( regressor, open( "linear_model.p", "wb" ) )
pickle.dump(onehotencoder,open( "linear_model_onehotencoder.p", "wb" ) )

zipcode=98002
bedrooms=3
bathrooms=2.5
floors=2
sqft_above=2000
sqft_basement=800
year_built=2010
sqft_living=2100
sqft_lot=2600

zipcode_loc =list(onehotencoder.active_features_).index(98002)
input_arr = np.zeros(len(list(onehotencoder.active_features_))-1)
input_arr[zipcode_loc-1] = 1
input_arr = np.append(input_arr, bedrooms)
input_arr = np.append(input_arr, bathrooms)
input_arr = np.append(input_arr, floors)
input_arr = np.append(input_arr, sqft_above)
input_arr = np.append(input_arr, sqft_basement)
input_arr = np.append(input_arr, year_built)
input_arr = np.append(input_arr, sqft_living)
input_arr = np.append(input_arr, sqft_lot)

print(regressor.predict([input_arr]))

#print(list(onehotencoder.active_features_).index(98002))
# 1. zipcode - int (All zipcodes except 98001 will be encoded as param #1 ~ due to dummy variable trap)
# 2. bedrooms - int 
# 3. bathrooms - float
# 4. floors - int
# 5. sqft_above - int
# 6. sqft_basement - int
# 7. year_built - int
# 8. zipcode - int
# 9. sqft_living - int
# 10. sqft_lot - int