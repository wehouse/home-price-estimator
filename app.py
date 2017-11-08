# -*- coding: utf-8 -*-

import falcon
from quote_resource import QuoteResource 




api = falcon.API()
api.add_route('/quote', QuoteResource())