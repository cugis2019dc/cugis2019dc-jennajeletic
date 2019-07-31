# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 10:04:40 2019

@author: STEM
"""

Cadbury1= "dark chocolate"
Cadbury2= "milk chocolate"
Cadbury3= "white chocolate"

DarkChoc=5
MilkChoc=6
WhiteChoc=8

print(Cadbury1, DarkChoc, Cadbury2, MilkChoc, Cadbury3, WhiteChoc)

WhiteChoc
Cadbury1

import pandas
dir(pandas)


choc1 = {"milk chocolate":6}
choc2 = {"dark chocolate":5}
choc3 = {"white chocolate":8}
print(choc1,choc2,choc3)
print(choc1)

chocolatebox = {"white chocolate":8,"dark chocolate":5,"milk chocolate":6}
chocolatebox
nameage = {"Steve":32,"Lia":28,"Vin":45,"Katie":38}
nameage

namegender = {"steve":"male","Lia":"female","vin":"male","katie":"female"}
namegender

studentlist = [['Steve',32,'male'],['Lia',28,'female'],
               ['Vin',45,'male'],['Katie',38,'female']]
studentlist

student = [nameage,namegender]
student

studentdf = pandas.DataFrame(studentlist)
studentdf

studentdf = pandas.DataFrame(studentlist,columns=("name","age","gender"))
studentdf

studentdf2 = pandas.DataFrame(studentlist,columns=("name","age","gender"),
                              index=["1","2","3","4"])
studentdf2

chocolateboxlist = [["milk",6],["dark",5],["white",8]]
chocolateboxdf= pandas.DataFrame(chocolateboxlist,columns=("Type","Amount"))
chocolateboxdf

#reference columns from dataframes
studentdf["name"]
studentdf["age"]
studentdf["gender"]

chocolateboxdf["Type"]
chocolateboxdf["Amount"]

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go

studentbar= go.Bar(x=studentdf["name"],y=studentdf["age"])
plot([studentbar])

chocolatebar = go.Bar(x=chocolateboxdf["Type"],y=chocolateboxdf["Amount"])
plot([chocolatebar])

titles = go.Layout(title = "Number of Chocolates by Type")

chocolatebar = go.Bar(x=chocolateboxdf["Type"],y=chocolateboxdf["Amount"])
#titling graph
fig = go.Figure(data=[chocolatebar], layout = titles)
plot(fig)
























