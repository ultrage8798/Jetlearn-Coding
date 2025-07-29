import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("covid_data.csv")
data.set_index("OBJECTID")

#print(data.head(5))

data = data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]
data.columns = ('State',"Country","Last Update","Lat","Long","Confirmed","Recovered","Deaths","Active")

#print(data.head(10))

import datetime as dt

def convertTime(t):
    t = int(t)
    return dt.datetime.fromtimestamp(t)

data = data.dropna(subset = ['Last Update'])
data["Last Update"] = data["Last Update"]/1000
data["Last Update"] = data["Last Update"].apply(convertTime)

print(data.head(10))

#10 most affected countries

top10_confirmed = pd.DataFrame(data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending = False))
#print(top10_confirmed)

fig1 = px.scatter(top10_confirmed,x = top10_confirmed.index,y="Confirmed",size = "Confirmed",size_max = 120, color = top10_confirmed.index,title = "Top 10 Countries by COnfirmed Case")
fig1.write_html("first_figure.html",auto_open = True)