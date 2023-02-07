# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:32:24 2023

@author: Gbenga Agunbiade
"""

import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
values = np.arange(1,7) 
prob = (0.1, 0.2, 0.3, 0.1, 0.1, 0.2) # probabilities must sum to 1
custm = stats.rv_discrete(values=(values, prob))

for i in range(20000):
    print(custm.rvs())