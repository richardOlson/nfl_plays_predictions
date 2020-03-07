import dash_daq as daq
import dash_core_components as dcc

timeGroup = [

    # Trying to make the quarter and the time grouped together


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
