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
import graficas


import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go


app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

imagen = [
                        html.Div([
                        html.Img(src='https://rockcontent.com/es/wp-content/uploads/sites/3/2019/02/Consejos-para-hacer-ima%CC%81genes-increi%CC%81bles.png.webp', style= {'width': '100%', 'display': 'inline-block'}),
                        ])
                ]

titulo = html.Title("Sell Sheet CMI",style={'width': '66%', 'display': 'inline-block','font-size':'5em','text-align':'center','vertical-align': 'top'})





app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
               dbc.CardBody(
                   imagen
               ) 
            ],className='mb-2'),
        ], width=3),
        dbc.Col([
            titulo
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
        ], width=4),
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
        ], width=5),
    ],className='mb-2 mt-2'),
dbc.Row([
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
            ]),
        ]),
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