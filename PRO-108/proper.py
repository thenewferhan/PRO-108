import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("data.csv")
#print(df)
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Height"],show_hist = False)
fig.show()