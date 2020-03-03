# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq


# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Use the drop-downs and sliders to choose the information you want to add. If you don't change
            anything the defaults shown will be used. 

            """
        ),
                
    
    
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Dropdown(
            options=[
            {'label': 'First Quarter', 'value': 1},
            {'label': 'Second Quarter', 'value': 2},
            {'label': 'Third Quarter', 'value': 3},
            {'label': 'Fourth Quarter', 'value':4},
            {'label': 'Overtime', 'value':5}
            ],
            value=1,
            placeholder="Select a Quarter",
            style={"background-color": "#f2f2f2", 'color':'black'}

        ),
        daq.NumericInput(
            id='minute',
            max=15,
            min=0,
            value=8
        )  
    ]
)

layout = dbc.Row([column1, column2])