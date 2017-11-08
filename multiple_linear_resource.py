# -*- coding: utf-8 -*-
from linear_model import KingCountyLinearModel

class MultipleLinearResource:
    kingC = KingCountyLinearModel()
    regressor,onehotencoder= kingC.create_regressor()

    def on_get(self, req, resp):
        
        
