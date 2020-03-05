# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_daq as daq


# Imports from this application
from app import app
from pickle import load

#load(open(fileName, 'rb')) C:\Users\rich\Richard_python\nfl_dash\nfl_plays_predictions\assets
theXgb = load(open(r'assets\xgb.pkl', 'rb'))


# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Use the drop-downs and text boxes to enter the information you want to add. These will then 
            be used to make the prediction if the next play is a Pass or a Run play.





            """
        ),
         html.Button(
            'Predict',
            id='predict_button',
            style={'width': '63%',  'color':'black', 'background-color': '#de7518',
                    'marginTop': '1em', 'marginBottom': '1em'}
         ),



        dcc.RadioItems(
            options=[
                {'label': 'Don\'t show probability',  'value': 'No'},
                {'label': 'Show Probability', 'value': 'Yes'},

            ],
            value='No'
        ),


    
    
    ],
    md=4,
)

column2 = dbc.Col(
    [
        
        dcc.Markdown(
            """
        
            Information about current play

            

            """
        ),

        html.Div(children=[
        html.Div(
            id="time",
            children=[
                dcc.Dropdown(
                    id='quarter',
                    options=[
                        {'label': '1st Qtr', 'value': 1},
                        {'label': '2nd Qtr' , 'value': 2},
                        {'label': '3rd Qtr', 'value': 3},
                        {'label': '4th Qtr', 'value': 4},
                        {'label': 'Overtime', 'value': 5},
                    ],
                    searchable=True,
                    placeholder="Quarter",
                    style={'width': '63%',  'color':'black', 'marginBottom': '1em',
                           'font-size':'small'}
                ), 

            
            # The minute input
                dcc.Input(
                    id='minute',
                    placeholder='Min',
                    persistence=True,
                    max=15,
                    min=0,
                    step=1,
                    type='number', 
                    style={'width': '20%', 'display': 'inline-block','marginBottom': '1em',
                           'font-size':'small'}
                ),#style={'width': '49%', 'display': 'inline-block'}

                # The seconds input
                  dcc.Input(
                    id='seconds',
                    placeholder='Sec',
                    persistence=True,
                    type='number',
                    max=59, 
                    min=0,
                    step=1,
                    value='', 
                    style={'width': '20%', 'display': 'inline-block','marginBottom': '1em', 'font-size':'small'}
                    ), 
                
                
                ]
        ), 
            html.Div(
                # The down
                dcc.Dropdown(
                    id='down',
                    options=[
                        {'label': '1st Down', 'value': 1},
                        {'label': '2nd Down', 'value': 2},
                        {'label': '3rd Down', 'value': 3},
                        {'label': '4th Down', 'value': 4},
                        
                    ],
                    searchable=True,
                    placeholder="Down",
                    style={'width': '63%',  'color':'black' ,'marginBottom': '1em'}
                ),

                    
            ),

            dcc.Input(
                        id='yard_to_go',
                        placeholder='Yards to Go',
                        persistence=True,
                        type='number',
                        max=100, 
                        min=0,
                        step=1,
                        value='', 
                        style={'width': '40%', 'display': 'inline-block','marginBottom': '1em',
                               'font-size':'small'}
                        ), 


            dcc.Dropdown(
                    id='formation',
                    options=[
                        {'label': 'Under Center', 'value': 'under_center'},
                        {'label': 'Shotgun', 'value': 'shotgun'},
                        {'label': 'No Huddle Shotgun', 'value': 'no_huddle_shotgun'},
                        {'label': 'No Huddle', 'value': 'no_huddle'},
                        {'label': 'Wildcat', 'value': 'wildcat'},
                        {'label': 'Other', 'value': 'nan'},
                    ],
                    searchable=True,
                    placeholder="Formation",
                    style={'width': '65%',  'color':'black', 'display': 'inline-block',
                           'font-size':'small'}
                ), 



        #style={'display': 'inline-block'})    
        ])

        
        
    ]
)

column3 = dbc.Col(
        [
            dcc.Markdown(
            """
        
            Information from previous  offensive play

            

            """
        ),

        dcc.Dropdown(
                    id='prev_down',
                    options=[
                        {'label': '1st Down', 'value': 1},
                        {'label': '2nd Down', 'value': 2},
                        {'label': '3rd Down', 'value': 3},
                        {'label': '4th Down', 'value': 4},
                        {'label': 'Two Point conv', 'value': 5},
                        
                    ],
                    searchable=True,
                    placeholder="Preious Down",
                    style={'width': '78%',  'color':'black' ,'marginBottom': '1em',
                           'font-size':'small'}
                ),


        dcc.Input(
                        id='yards_needed',
                        placeholder='Yards for 1st down',
                        persistence=True,
                        type='number',
                        max=100, 
                        min=0,
                        step=1,
                        value='', 
                        style={'width': '60%', 'display': 'inline-block','marginBottom': '1em' ,
                               'font-size':'small'}
                        ),

        dcc.Input(
                        id='yards_gained',
                        placeholder='Yards gained',
                        persistence=True,
                        type='number',
                        max=100, 
                        min=-99,
                        step=1,
                        value='', 
                        style={'width': '60%', 'display': 'inline-block','marginBottom': '1em'}
                        ),


        html.Div(
            dcc.Dropdown(
                        id='prev_play',
                        options=[
                            {'label': 'Pass', 'value': 'Pass'},
                            {'label': 'Run', 'value': 'Rush'},
                            
                        ],
                        searchable=True,
                        placeholder="Play Type",
                        style={'width': '78%',  'color':'black', 'display': 'inline-block','marginBottom': '.3em',
                               'font-size':'small'}
                    ), 
        ),
        dcc.Dropdown(
                id='what_happened',
                options=[
                    {'label':'Normal Play', 'value': 'nothing'},
                    {'label':'Touch Down', 'value': 'touchDown'},
                    {'label':'Fumble', 'value': 'fumble'},
                    {'label':'Interception', 'value': 'interception'},
                    {'label':'Safety', 'value': 'nothing'},

                ], 
                searchable=True,
                placeholder="Result of Play",
                style={'width': '78%',  'color':'black', 'display': 'inline-block','marginBottom': '.3em'}

        ),




        ]
)

layout = html.Div(
    [


    dbc.Row([column1, column2, column3]),
    dbc.Row(dbc.Col(html.Div(id="predHere", ),
                    width={"size": 6, "offset": 3},))

    ]
)




@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value')])
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)

