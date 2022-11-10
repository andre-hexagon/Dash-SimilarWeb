import plotly.graph_objects as go
import pandas as pd

def TemporalGraph1(t,x1):
    fig = go.Figure([go.Scatter(x=t,y=x1)])
    fig.update_xaxes(
        title_text = "Lorem Ipsum X",
        title_font = {"size": 20})
    fig.update_yaxes(
        title_text = "Lorem Ipsum Y",
        title_font = {"size": 20})

    return(fig.show())
  
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
