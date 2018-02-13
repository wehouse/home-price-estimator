# -*- coding: utf-8 -*-

import falcon
from falcon_cors import CORS

from multiple_linear_resource import MultipleLinearResource 

public_cors = CORS(allow_all_origins=True, allow_all_methods=True, allow_all_headers=True, allow_headers_list=['Content-Type'])


api = falcon.API(middleware=[public_cors.middleware])
api.add_route('/multiple-linear', MultipleLinearResource())