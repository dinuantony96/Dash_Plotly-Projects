import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash

from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

#-----------------------------------------
# Importing and Cleaning Data
#-----------------------------------------

data = pd.read_csv('./data/bees.csv')

data = data.groupby(['State','ANSI','Affected by','Year','state_code'])[['Pct of Colonies Impacted']].mean()
data.reset_index(inplace=True)

#-----------------------------------------
# App Layout
#-----------------------------------------

app.layout = html.Div([

    html.H1("Web Application Dashboard with Dash", style={'text-align':'center'}),

    dcc.Dropdown(id="select_year",
                 options=[
                     {"label":"2015","value":2015},
                     {"label":"2016","value":2016},
                     {"label":"2017","value":2017},
                     {"label":"2018","value":2018}],
                 multi=False,
                 value=2015,
                 style={'width':'40%'}
                 ),
    
    html.Div(id='output_container',children=[]),
    html.Br(),

    dcc.Graph(id='bee_map',figure={})

])

#-----------------------------------------
# End of Program
#-----------------------------------------
