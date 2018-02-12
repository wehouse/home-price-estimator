# -*- coding: utf-8 -*-

import falcon
from falcon_cors import CORS

from multiple_linear_resource import MultipleLinearResource 


public_cors = CORS(allow_all_origins=True, allow_all_headers=True)


api = falcon.API(middleware=[public_cors.middleware])
api.add_route('/multiple-linear', MultipleLinearResource())