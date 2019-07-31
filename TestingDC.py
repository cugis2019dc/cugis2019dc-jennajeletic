#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 07:55:28 2019

@author: rogersentongo
"""

import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go



data = float(input("What is the value you want?"))

def Area(a,b):
    value = a*b
    print(value)
    
Area(data, 2)    


