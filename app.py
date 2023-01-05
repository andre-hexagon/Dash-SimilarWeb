import nltk
nltk.download('stopwords')

import sql_connection_class
from graficas import *
from email.mime import image
from turtle import width
from dash import Dash, html
from dash import dcc
from dash.dependencies import Output, Input

import plotly.graph_objects as go

from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from datetime import date
import calendar


import plotly
import plotly.graph_objects as go


# SQL = sql_connection_class.sql_connection()
# query_groupedTotal = "SELECT * FROM SW_GROUPED_TOTAL limit 5000"
# query_groupedByMonth = "SELECT * FROM SW_GROUPED_BY_MONTH limit 5000"
# df = SQL.exec_query(query_groupedTotal)
# df.rename(columns={col:col.lower() for col in df.columns},inplace=True)

# dfMonth = SQL.exec_query(query_groupedByMonth)
# dfMonth.rename(columns={col:col.lower() for col in dfMonth.columns},inplace=True)

# print(df.columns)
# print(df['main_category'].head())
df = pd.read_csv('MOCK_DATA.csv')
dfMonth = pd.read_csv('MOCK_DATA.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

imagen = [
            html.Div([
            html.Img(src='https://www.hexagondata.com/wp-content/uploads/2020/07/13_35_17.png', style= {'width': '50%', 'display': 'inline-block'}),
            ])
        ]

titulo = html.Title("Sell Sheet CMI",style={'width': '66%', 'display': 'inline-block','font-size':'5em','text-align':'center','vertical-align': 'top'})

texto = html.Div([
    # html.H6(insight_trend(df))
])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            imagen
            , width=3),
        dbc.Col([
            titulo
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Número total de interacciones",style={'text-align': 'center'}),
                    dcc.Graph(figure=plot_indicator(df,'estimated_views')) 
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Comportamiento semanal de vistas y compras por usuario",style={'text-align': 'center'}),
                    dcc.Graph(figure=TemporalGraph1(dfMonth['month'],dfMonth['estimated_views']))
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
     dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardBody([
                    texto
                ]) 
            ],className='mb-2'),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=TemporalGraph2(dfMonth['month'],dfMonth['estimated_views'],dfMonth['estimated_views']))
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardBody([
                    html.H6("Proporcion de las ventas respecto al total de interacciones de usuarios",style={'text-align': 'center'}),
                    dcc.Graph(figure=bar(df,972))
                ]) 
            ],className='mb-2'),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardBody([
                    dcc.Graph(figure=barCloud(df,972))
                ]) 
            ],className='mb-2'),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Nube de palabras de productos más vistos",style={'text-align': 'center'}),
                    dcc.Graph(figure=plot_wordcloud(df,'estimated_views'))
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Nube de palabras de productos más comprados",style={'text-align': 'center'}),
                    dcc.Graph(figure=plot_wordcloud(df,'estimated_purchases'))
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardBody([
                    html.H6("Proporción del total de ventas por categoría",style={'text-align': 'center'}),
                    dcc.Graph(figure=pie(df,972))
                ]) 
            ],className='mb-2'),
        ], width=8),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardBody([
                    html.H6("Performance por marca",style={'text-align': 'center'}),
                    dcc.Graph(figure=dispersion(df,"brand"))
                ]) 
            ],className='mb-2'),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H6("Performance por producto",style={'text-align': 'center'}),
                   dcc.Graph(figure=dispersion(df,"main_category")) 
                ])
            ]),
        ], width=6),
    ],className='mb-2 mt-2')
    ], fluid=True)


if __name__ == '__main__':
    app.run_server(debug=True, port=8002)




# def description_card():
#     """
#     :return: A Div containing dashboard title & descriptions.
#     """
#     return html.Div(
#         id="description-card",
#         children=[
#             html.H5("Clinical Analytics"),
#             html.H3("Welcome to the Clinical Analytics Dashboard"),
#             html.Div(
#                 id="intro",
#                 children="Explore clinic patient volume by time of day, waiting time, and care score. Click on the heatmap to visualize patient experience at different time points.",
#             ),
#         ],
#     )