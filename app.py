# -*- coding: utf-8 -*-

import falcon
from multiple_linear_resource import MultipleLinearResource 
from gradient_boosting_regression_resource import GradientBoostingResource



api = falcon.API()
api.add_route('/multiple-linear', MultipleLinearResource())
api.add_route('/gradient-boost', GradientBoostingResource())