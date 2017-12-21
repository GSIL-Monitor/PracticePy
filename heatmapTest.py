# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:35:40 2017

@author: fmeng
"""

import numpy as np
import seaborn as sns
uniform_data = np.random.rand(10, 12)
ax = sns.heatmap(uniform_data)