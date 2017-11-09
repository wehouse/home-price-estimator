# -*- coding: utf-8 -*-

import falcon
from multiple_linear_resource import MultipleLinearResource 




api = falcon.API()
api.add_route('/multiple-linear', MultipleLinearResource())