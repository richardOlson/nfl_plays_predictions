# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import  plotly.graph_objects as go
from  pickle import load
import pandas as pd

# Imports from this application
from app import app


teamAcc = load(open(r"assets\teamAccuracy.pkl", "rb"))

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Is the next play a run or a pass play?



            Can you tell if the next play will be a run or a pass play?


            Use the predict portion of this app to predict what kind of play will be next.

            Check out the graph for plays from Sept 23, 2019 to the end of 2019 season.  Which NFL teams are the most predictable.  Does this predictability matter to their success? 

            

            """
        ),
        dcc.Link(dbc.Button('Predict the next play', color='primary'), href='/predictions')
    ],
    md=4,
)

fig = go.Figure(data=[
    go.Bar( name='Accuracy', x=teamAcc.index, y=teamAcc['Accuracy']),
    go.Bar(name='AUC', x=teamAcc.index, y=teamAcc['AUC'])
])

# Change the bar mode
fig.update_layout(barmode='group', legend=dict(x=-.1, y=1.2), margin=dict(
        l=0,
        r=10,
        b=100,
        t=100,
        pad=3
    ),
    paper_bgcolor="LightSteelBlue",)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1 , column2])