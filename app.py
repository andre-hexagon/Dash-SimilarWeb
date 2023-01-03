import plotly.graph_objects as go
import plotly
import calendar
from datetime import date
import pandas as pd                      # pip install pandas
import plotly.express as px              # pip install plotly
# pip install dash-bootstrap-components
import dash_bootstrap_components as dbc
from dash_extensions import Lottie       # pip install dash-extensions
from dash.dependencies import Output, Input
from dash import dcc
from dash import Dash, html
from turtle import width
from email.mime import image
from graficas import *
import nltk
nltk.download('stopwords')


df = pd.read_csv('MOCK_DATA.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

imagen = [
    html.Div([
        html.Img(src='https://www.hexagondata.com/wp-content/uploads/2020/07/13_35_17.png',
                 style={'width': '50%', 'display': 'inline-block'}),
    ])
]

titulo = html.Title("Sell Sheet CMI", style={
                    'width': '66%', 'display': 'inline-block', 'font-size': '5em', 'text-align': 'center', 'vertical-align': 'top'})

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            imagen, width=3),
        dbc.Col([
            titulo
        ]),
    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=TemporalGraph1(
                        df['month'], df['estimated_views']))
                ])
            ]),
        ]),
    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ], className='mb-2'),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=TemporalGraph2(
                        df['month'], df['estimated_views'], df['estimated_views']))
                ])
            ]),
        ]),
    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(figure=plot_wordcloud(df, 'categoria2'))
                ])
            ], className='mb-2'),
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ]),
    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ], className='mb-2'),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ]),
    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ], className='mb-2'),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=5),
    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ], className='mb-2'),
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=6),
    ], className='mb-2 mt-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ]),
    ], className='mb-2 mt-2'),
], fluid=True)


if __name__ == '__main__':
    app.run_server(debug=True, port=8002)
