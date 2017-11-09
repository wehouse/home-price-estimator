# -*- coding: utf-8 -*-
import pickle
import numpy as np

class MultipleLinearResource:
    linear_model={}
    onehotencoder = {}
    def __init__(self):
        self.linear_model = pickle.load( open( "linear_model.p", "rb" ) )
        self.onehotencoder = pickle.load(open('linear_model_onehotencoder.p', 'rb'))
        
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
        print(json.get('zipcode'))
        zipcode_loc =list(self.onehotencoder.active_features_).index(json.get('zipcode'))
        input_arr = np.zeros(len(list(self.onehotencoder.active_features_))-1)
        input_arr[zipcode_loc-1] = 1
        input_arr = np.append(input_arr, json.get('bedrooms'))
        input_arr = np.append(input_arr, json.get('bathrooms'))
        input_arr = np.append(input_arr, json.get('floors'))
        input_arr = np.append(input_arr, json.get('sqft_above'))
        input_arr = np.append(input_arr, json.get('sqft_basement'))
        input_arr = np.append(input_arr, json.get('year_built'))
        input_arr = np.append(input_arr, json.get('sqft_living'))
        input_arr = np.append(input_arr, json.get('sqft_lot'))
        resp.media = self.linear_model.predict([input_arr])[0]