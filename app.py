import nltk
nltk.download('stopwords')

import sql_connection_class
from graficas import *
from email.mime import image
from turtle import width
from dash import Dash, html
from dash import dcc
from dash.dependencies import Output, Input

from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from datetime import date
import calendar


import plotly
import plotly.graph_objects as go


SQL = sql_connection_class.sql_connection()
query_str = "SELECT * FROM similar_web_raw where main_category not in ('N/A') limit 5000"
df = SQL.exec_query(query_str)

print(df.columns)
print(df['main_category'].head())
# df = pd.read_csv('MOCK_DATA.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

imagen = [
            html.Div([
            html.Img(src='https://www.hexagondata.com/wp-content/uploads/2020/07/13_35_17.png', style= {'width': '50%', 'display': 'inline-block'}),
            ])
        ]

titulo = html.Title("Sell Sheet CMI",style={'width': '66%', 'display': 'inline-block','font-size':'5em','text-align':'center','vertical-align': 'top'})

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
                    dcc.Graph(figure=TemporalGraph1(df['month'],df['estimated_views']))
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardBody([
                    
                ]) 
            ],className='mb-2'),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=TemporalGraph2(df['month'],df['estimated_views'],df['estimated_views']))
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardBody([
                     dcc.Graph(figure=plot_wordcloud(df))
                ]) 
            ],className='mb-2'),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=barCloud(df,972))
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardBody([
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
                ]) 
            ],className='mb-2'),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=5),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    ]) 
                ],className='mb-2'),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=6),
    ],className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ]),
    ],className='mb-2 mt-2'),
    ], fluid=True)


if __name__ == '__main__':
    app.run_server(debug=True, port=8002)