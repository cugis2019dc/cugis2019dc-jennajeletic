# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 11:47:08 2019

@author: STEM
"""

import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

womencancerdf = pd.read_excel("GISdatajj.xlsx", sheet_name = "cancercases")
womencancerdf

womenwithcancer = go.Bar(x= womencancerdf["CancerType"],y= womencancerdf["Number"],
                         marker = {"color":womencancerdf["Number"],"colorscale" : "Bluered"})
titles = go.Layout(title = "Number of Women with Certain Types of Cancer",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Type of Cancer")),
                   yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Number of Women")))

fig = go.Figure(data=[womenwithcancer], layout = titles)
plot(fig)


plot([womenwithcancer])
