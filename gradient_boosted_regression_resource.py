# -*- coding: utf-8 -*-
import pickle
import numpy as np

class GradientBoostedRegressionResource:
    boosted_regression_model={}
    def __init__(self):
        self.boosted_regression_model = pickle.load( open( "boosted_regression.p", "rb" ) )
        
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

    def on_post(self, req, resp):      
        json = req.media
        input_arr = []
       
        input_arr = np.append(input_arr, json.get('date'))
        input_arr = np.append(input_arr, json.get('bedrooms'))
        input_arr = np.append(input_arr, json.get('bathrooms'))
        input_arr = np.append(input_arr, json.get('sqft_living'))
        input_arr = np.append(input_arr, json.get('sqft_lot'))
        input_arr = np.append(input_arr, json.get('floors'))
        input_arr = np.append(input_arr, json.get('waterfront'))
        input_arr = np.append(input_arr, json.get('view'))
        input_arr = np.append(input_arr, json.get('condition'))
        input_arr = np.append(input_arr, json.get('grade'))

        input_arr = np.append(input_arr, json.get('sqft_above'))
        input_arr = np.append(input_arr, json.get('sqft_basement'))
        input_arr = np.append(input_arr, json.get('year_built'))
        input_arr = np.append(input_arr, json.get('year_renovated'))
        input_arr = np.append(input_arr, json.get('zipcode'))
        input_arr = np.append(input_arr, json.get('lat'))
        input_arr = np.append(input_arr, json.get('long'))
        input_arr = np.append(input_arr, json.get('sqft_living15'))
        input_arr = np.append(input_arr, json.get('sqft_lot'))
        resp.media = self.boosted_regression_model.predict([input_arr])[0]