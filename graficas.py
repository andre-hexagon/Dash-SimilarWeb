import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import numpy as np
from PIL import Image
from matplotlib import pyplot
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.corpus import stopwords
stop = stopwords.words("spanish")


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

    return(fig)

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

    return(fig)


################################################## 
######### Nube de Palabras por categoría #########
##################################################
def plot_wordcloud(df,category):
    dfc = df[df['main_category'].str.contains(category)]
    dfc['tokenized_title']=dfc['title'].str.split(" ",expand = False)
    dfc['title']=dfc['title'].str.lower()
    dfc['title_wo_stopwords']=dfc['title'].apply(lambda x:[item for item in str(x).split() if item not in stop])
    dfc3p = dfc.loc[dfc.index.repeat(dfc.estimated_purchases)]
    dfc3p = dfc3p.reset_index()
    text_cp=[]
    for i in range(0,len(dfc3p)):
        text_cp += dfc3p.title_wo_stopwords[i]
    text_cp
    text1_cp= " ".join(text_cp)
    text2_cp = text1_cp.replace(',','')
    text2_cp
    wc = WordCloud(background_color='white', width=1080, height=360)
    wc.generate(text2_cp)

    img = wc.to_image()

    # Convert the image string to numpy array and create a
    # Plotly figure, see https://plotly.com/python/imshow/
    fig = px.imshow(np.array(img))

    # Hide the axes and the tooltips
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=20, b=0, l=0, r=0),
        xaxis=dict(
            showgrid=False,
            showticklabels=False,
            linewidth=0
        ))
        
    return(fig)
######################prueba##############################
plot_wordcloud(df,'Alimentos y Bebidas', 972)
