import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

################################################## 
######### Gráficas Temporales (1 Curvas) #########
##################################################

def TemporalGraph1(t,x1):
    fig = go.Figure([go.Scatter(x=t,y=x1)])
    fig.update_xaxes(
        title_text = "Lorem Ipsum X",
        title_font = {"size": 20})
    fig.update_yaxes(
        title_text = "Lorem Ipsum Y",
        title_font = {"size": 20})

    return(fig.show())

################################################## 
######### Gráficas Temporales (2 Curvas) #########
##################################################
  
def TemporalGraph2(t,y1,y2):
    fig = go.Figure([
        go.Scatter(
            x=t,y=y1,name='Bel'
        ),
        go.Scatter(
            x=t,y=y2,name='Bel'
        )
    ])
    
    fig.update_xaxes(
        title_text = "Lorem Ipsum X",
        title_font = {"size": 20})
    fig.update_yaxes(
        title_text = "Lorem Ipsum Y",
        title_font = {"size": 20})

    return(fig.show())
