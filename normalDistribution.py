import csv
import statistics as st
from typing import Match
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
math=df["math score"].tolist()
mean=st.mean(math)
median=st.median(math)
mode=st.mode(math)
sd=st.stdev(math)
print(mean,mode,median,sd)
sd1start,sd1end=mean- sd, mean+ sd
sd2start,sd2end=mean-(2*sd),mean+(2*sd)
sd3start,sd3end=mean-(3*sd),mean+(3*sd)
fig=ff.create_distplot([math],["math scores"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[sd1start,sd1start],y=[0,0.17],mode="lines",name="first Standard deviation"))
fig.add_trace(go.Scatter(x=[sd1end,sd1end],y=[0,0.17],mode="lines",name="first Standard deviation"))
fig.add_trace(go.Scatter(x=[sd2start,sd2start],y=[0,0.17],mode="lines",name="second Standard deviation"))
fig.add_trace(go.Scatter(x=[sd2end,sd2end],y=[0,0.17],mode="lines",name="second Standard deviation"))
fig.add_trace(go.Scatter(x=[sd3start,sd3start],y=[0,0.17],mode="lines",name="third Standard deviation"))
fig.add_trace(go.Scatter(x=[sd3end,sd3end],y=[0,0.17],mode="lines",name="third Standard deviation"))

listofDataWithinOnesd=[result for result in math if result>sd1start and result<sd1end]
listofDataWithintwosd=[result for result in math if result>sd2start and result<sd2end]
listofDataWithinthreesd=[result for result in math if result>sd3start and result<sd3end]
print("{}% of data lies within first standard deviation".format(len(listofDataWithinOnesd)*100/len(math)))
print("{}% of data lies within second standard deviation".format(len(listofDataWithintwosd)*100/len(math)))
print("{}% of data lies within third standard deviation".format(len(listofDataWithinthreesd)*100/len(math)))
fig.show()