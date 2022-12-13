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
nltk.download('stopwords')
stop = stopwords.words("spanish")
import nltk
import re


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


################################################## 
############# Tarjeta de Resultados ##############
##################################################

def plot_indicator(df,metric):
    #write a plotly function with go.Indicator to plot the metric of interest without delta#
    #df is the dataframe with the data#
    #metric is the metric of interest#
    #return the plotly figure#

    fig=go.Figure(go.Indicator(
        mode = "number",
        value = df[metric].iloc[0],
        title = {"text": metric},
        domain = {'x': [0, 1], 'y': [0, 1]}))

    return(fig)

################################################## 
######### Nube de Palabras con barritas###########
##################################################

def plot_wordcloud(df,category, w, mode = 'RGB',file_ouput = 'image.png', variable = 'sub_sub_category'):
    df = df[df[variable].isnull() == False]
    dfc = df[df[variable].str.contains(category)]     
    dfc['title_wo_stopwords'] = dfc['title'].apply(lambda x: [x.lower() for x in re.findall(r'\w+',str(x)) if x.isalpha() and x not in stop and len(x) > 2])
    dfc3p = dfc.loc[dfc.index.repeat(dfc.estimated_views)]
    dfc3p = dfc3p.reset_index()
    text_cp=[]
    for i in range(0,len(dfc3p)):
        text_cp += dfc3p.title_wo_stopwords[i]
    text_cp
    text1_cp= " ".join(text_cp)
    text2_cp = text1_cp.replace(',','')
    text2_cp
    wc = WordCloud(mode=mode,width=w, height=210, random_state = 77300, 
                            background_color = None, collocations=False).generate(text2_cp)
    wc.to_file(file_ouput)

def barCloud(df, w, variable = 'sub_sub_category', mode = 'RGB', top = 5):
    w = w
    variable = variable
    df_group = df[[variable,'estimated_views']].groupby(variable, as_index=False)\
                                                .sum()\
                                                .sort_values('estimated_views',ascending = False)[:top]\
                                                .sort_values('estimated_views')\
                                                .reset_index(drop = True)
    
    df_group['estimated_views'] = df_group.estimated_views.apply(int)
    lista_images = df_group[variable].to_list()

    for n, images in enumerate(lista_images):
        file_name = "image{}.png".format(n+1)
        plot_wordcloud(df, images, w, file_ouput = file_name, mode = mode)
    
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x= df_group.estimated_views.to_list(),
            y= df_group[variable].to_list(),
            marker=go.bar.Marker(
                color="rgb(256, 256, 256)",
                line=dict(color="rgb(0, 0, 0)",
                          width=2)
            ),
            orientation="h",
        )
    )

    # Add images
    for i, row in df_group.iterrows():
        fig.add_layout_image(
                dict(
                    source=Image.open("image{}.png".format(i+1)),
                    xref="x",
                    yref="y",
                    xanchor="center",
                    yanchor="middle",
                    x=row[1] * 0.501,
                    y=row[0],
                    sizex= row[1],
                    sizey= 0.8,
                    sizing="stretch",
                    layer="above")
        )

    # update layout properties
    fig.update_layout(
        autosize=False,
        height=900,
        width=1000,
        bargap=0.15,
        bargroupgap=0.1,
        barmode="stack",
        hovermode="x",
        margin=dict(r=20, l=300, b=75, t=125)
    )

    fig.show()
    
################################################## 
############## Barritas  Sencillas################
##################################################

    def bar(df, w, variable = 'sub_sub_category', top=7):
    w = w
    variable = variable
    df_group = df[[variable,'estimated_views']].groupby(variable, as_index=False)\
                                                .sum()\
                                                .sort_values('estimated_views',ascending = False)[:top]\
                                                .sort_values('estimated_views')\
                                                .reset_index(drop = True)
    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x= df_group.estimated_views.to_list(),
            y= df_group[variable].to_list(),
            marker=go.bar.Marker(
                color="rgb(32, 115, 236)",
                line=dict(color="rgb(0, 0, 0)",
                          width=2)
            ),
            orientation="h",
        )
    
    )
        # update layout properties
    fig.update_layout(
        autosize=False,
        height=700,
        width=1000,
        bargap=0.15,
        bargroupgap=0.1,
        barmode="stack",
        hovermode="x",
        margin=dict(r=20, l=300, b=75, t=125)
    )
    
    fig.show()
    
################################################## 
##################### Gráfica Pie ################
##################################################

    def pie(df, w, variable = 'sub_sub_category', top=7):
    w = w
    variable = variable
    df_group = df[[variable,'estimated_views']].groupby(variable, as_index=False)\
                                                .sum()\
                                                .sort_values('estimated_views',ascending = False)[:top]\
                                                .sort_values('estimated_views')\
                                                .reset_index(drop = True)
    fig = px.pie(df_group.estimated_views.to_list(), df_group[variable].to_list())
    return(fig)
