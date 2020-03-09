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
import pandas as pd



# Getting the xgb and the features that we need for the model
#load(open(fileName, 'rb')) C:\Users\rich\Richard_python\nfl_dash\nfl_plays_predictions\assets
theXgb = load(open("assets/xgb.pkl", "rb"))
featuresDataFrame = load(open("assets/features.py", "rb"))


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
            id="show_proba",
            options=[
                {'label': 'Don\'t show probability ',  'value': 0},
                {'label': 'Show Probability', 'value': 1},


            ],
            labelStyle={'width': '50%'},
            value=0
        ),

        html.Div(id="predHere",
                        style={'width': '75%',
                           'font-size':'large', 'color':'#de7518' }
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

        html.Div(
            children=[
                html.Div(children=[

                html.Div(
                    "Offense   ",
                    style={'width': '20%',
                           'font-size':'small', 'display':'inline-block', 'marginRight':'2em'}
                ),

                html.Div(
                    "Defense",
                    style={'width': '20%',
                           'font-size':'small', 'display':'inline-block'}
                ),

                    ]

                ),


                    dcc.Input(
                        id='offense_score',
                        placeholder='score',
                        persistence=True,
                        max=99,
                        #value=0,
                        min=0,
                        step=1,
                        type='number',
                        style={'display': 'inline-block','marginBottom': '1em',
                               'font-size':'small', 'width': '25%'}
                    ),

                        dcc.Input(
                            id='defense_score',
                            placeholder='score',
                            type='number',
                            persistence=True,
                            #value=0,
                            max=99,
                            min=0,
                            step=1,

                            style={'display': 'inline-block','marginBottom': '1em',
                                   'font-size':'small', 'width': '25%'}
                        ),
                    ],





        ),
            html.Div(children =[

                dcc.Input(
                            id='yard_line',
                            placeholder='yard line',
                            type='number',
                            persistence=True,
                            max=50,
                            #value=0,
                            min=0,
                            step=1,

                            style={'display': 'inline-block','marginBottom': '.5em',
                              'font-size':'x-small', 'width': '50%'}


                ),


            dcc.RadioItems(
                        id="own_yard_line",
                        options=[
                            {'label': 'Own',  'value': 1},
                            {'label': 'Opposing', 'value': 0},



                        ],
                        labelStyle={'font-size':'x-small'},
                        value=0,
                        style={'display': 'inline-block', 'marginBottom': '1em', 'marginLeft':'1em' ,
                               'marginTop':'0em', 'font-size': 'small', 'width': '50%'}
                    ),
            ],
                    style={'marginBottom': '.5em',
                              'font-size':'x-small', 'width': '100%'}

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
                    #value=1,
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
                    type='number',
                    max=15,
                    min=0,
                    step=1,

                    #value=15,

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
                    #value=0,
                    step=1,

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
                        {'label': 'Two Point Conv', 'value': 5},
                    ],
                    #value=1,
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
                        #value=0,
                        style={'width': '40%', 'display': 'inline-block','marginBottom': '1em',
                               'font-size':'small'}
                        ), 


            dcc.Dropdown(
                    id='formation',
                    options=[
                        {'label': 'Under Center', 'value': 'Formation_UNDER CENTER'},
                        {'label': 'Shotgun', 'value': 'Formation_SHOTGUN'},
                        {'label': 'No Huddle Shotgun', 'value': 'Formation_NO HUDDLE SHOTGUN'},
                        {'label': 'No Huddle', 'value': 'Formation_NO HUDDLE'},
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
                        {'label': 'Two Point conv.', 'value': 5},
                        
                    ],
                    searchable=True,
                    placeholder="Preious Down",
                    style={'width': '78%',  'color':'black' ,'marginBottom': '1em',
                           'font-size':'small'}
                ),

            dcc.Input(
                        id='yards_gained',
                        placeholder='Yards gained',
                        persistence=False,
                        type='number',
                        max=100,
                        min=-99,
                        step=1,
                        #value=0,
                        style={'width': '60%', 'display': 'inline-block','marginBottom': '1em'}
                        ),

        dcc.Input(
                        id='yards_needed',
                        placeholder='Yards to go',
                        persistence=False,
                        type='number',
                        max=100, 
                        min=0,
                        step=1,
                        #value=0,
                        style={'width': '60%', 'display': 'inline-block','marginBottom': '1em' ,
                               'font-size':'small'}
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
                    {'label':'Normal Play', 'value': 'normal'},
                    {'label':'Touch Down', 'value': 'touchDown'},
                    {'label':'Fumble', 'value': 'fumble'},
                    {'label':'Interception', 'value': 'interception'},
                    {'label':'Safety', 'value': 'safety'},

                ],
                value='normal',
                searchable=True,
                placeholder="Result of Play",
                style={'width': '78%',  'color':'black', 'display': 'inline-block','marginBottom': '.3em'}

        ),




        ]
)

# This is the layout for the page
layout = html.Div(
    [


    dbc.Row([column1, column2, column3]),
    dbc.Row(dbc.Col(
                    width={"size": 6, "offset": 3},))

    ]
)


# Creating a method to make the seconds till end of game
def makeSecondsTillEnd(min_val, sec_val, quarter_val):
    if quarter_val == 5:
        ans = (min_val * 60) + sec_val
        # Overtime is for only 10 minutes
        ans = ((600 - ans) * -1)
        return ans
    else:
        ans = ((4 - quarter_val) * 900) + (min_val * 60) + sec_val
        return ans


# Function to fill in the previous plays
# 'prev_offense_play_Pass',
# 'prev_offense_play_Rush',
def makePrevPlay(prev_play_val, theList):
  if prev_play_val == "Pass":
    theList.append(('prev_offense_play_Pass', 1))
    theList.append(('prev_offense_play_Rush', 0))
  else:
    theList.append(('prev_offense_play_Pass', 0))
    theList.append(('prev_offense_play_Rush', 1))

  return theList


# making columns for each down
# Trying to see if this will make model see the importance of the down that it is on
# This method will drop the toGo and the down features
def makeDownCols(theList, down_val, yard_to_go_val):
    downsList = ['first_to_go',
                 'second_to_go',
                 'third_to_go',
                 'fourth_to_go',
                 'two_point_to_go']

    for i in range(len(downsList)):
        if down_val == i + 1:
            theList.append((downsList[i], yard_to_go_val))
        else:
            theList.append((downsList[i], 0))
    return theList

    # Functions for making the prev play categories


# creating the function that will categorize
# how succesfull a play is.
# Folowing what was determined by
# Bob Carroll and Pete Palmer and John Thorn, in their
# book called "The Hidden Game of Football".
# Also using a method similar to those on Footballoutsiders.com

# First Down play need --- 45% of required yards (yards for first down)to get a point
# Second Down play needs-- 60% of required yards (yards for first down)
# Third and Forth need 100 % of required yards to first down to be succes

def getPercentage(down, distance):
    if down == 4 or down == 3:
        return distance
    if down == 2:
        return distance * .6
    if down == 1:
        return distance * .45
        # returning this if for some reason a down is 0
    if down == 0:
        return 1


# Inner method that will make all the necesarry
# Loading of all the wanted categories
def getCompletedList(catListPass, catListRun, catNamesRun, catNamesPass):
    # the list to return
    finalList = []
    # this is a list that is a
    # combo of the catListRun and the catListPass
    cmp = catListRun + catListPass
    # complete list of the names
    nameComp = catNamesRun + catNamesPass

    theList = [

        'prev_offense_play_No Previous',
             'prev_ply_bad_run',
             'prev_ply_bad_pass',
             'prev_ply_no_succ_run',
             'prev_ply_no_succ_pass',
             'prev_ply_little_succ_pass',
             'prev_ply_mild_succ_run',
             'prev_ply_mild_succ_pass',
             'prev_ply_succ_run',
             'prev_ply_succ_pass',
             'prev_ply_high_succ_run',
             'prev_ply_high_succ_pass',

    ]
    finalList.append(('prev_offense_play_No Previous', 0))
    for i in range(1, len(theList)):
        for j in range(len(nameComp)):
            if nameComp[j] == theList[i]:
                finalList.append((nameComp[j], cmp[j]))

    return finalList


# This is an inner method that will load the
# categories with the score
# I am using this method instead of a pandas cut
# because I already am looping through
# the dataframe to get the score so at the
# same time will make the categories
def fillOtherCat(numberToSkip, catList):
    for i in range(len(catList)):
        if numberToSkip != i:
            catList[i] = 0
    return catList


# This is the method that will load the categories with the correct value
def loadBothCategories(catListRun_, catListPass_, score, thePlayType, theBins,
                       catNamesRun, catNamesPass):
    fillAll = 100

    if thePlayType == 'Rush':
        # We will do the binning of the score in the categories
        # for a Run play # will only loop to be able to put in each category
        for i in range(len(theBins)):
            # if the score is greater than upper bin
            # the the score must be placed in a lower bin
            if score < theBins[i]:
                catListRun_[i] = score
                catListRun_ = fillOtherCat(i, catListRun_)
                # Filling in all the Pass categories with a zero
                catListPass_ = fillOtherCat(fillAll, catListPass_)
                return getCompletedList(catListPass_, catListRun_,
                                        catNamesRun, catNamesPass)

    # bins = [0, .20, .26, .51, 1.0, 2, 99]
    else:
        for i in range(len(theBins)):
            # if the score is greater than upper bin
            # the the score must be placed in a lower bin
            if score < theBins[i]:
                catListPass_[i] = score
                catListPass_ = fillOtherCat(i, catListPass_)
                # Filling in all the categories for run as zero
                catListRun_ = fillOtherCat(fillAll, catListRun_)
                return getCompletedList(catListPass_, catListRun_,
                                        catNamesRun, catNamesPass)


# Succesfull play == 1 point
# Unsuccesfull play = 0 points
# Fractional points for can by if yards are gained but not the complete
# required for the down
# First Fractional (yardsGained/YardsNeededFor45%ToFirstDown - ( .1)
# Second Fraction  (yardsGained/YardsNededFor60%ToFirstDown) -(.2)
# Third Fraction (yardsGained/YardsNeededToFirstDown) - .3
# Fourth Fraction --No Fraction if not succesfull

# Fumble == minus 2
# Interception == minus 4
# loss of 3 yards or more minus 1 point

# Got a TouchDown plus  1 point
# Gained 15 yards 1 point
# If got a first down on a fourth down get an extra point

# Categories:
# High Success = 2 points
# Sucessfull = 1 points up to 2
# SomeWhatSucessfull =  .5 to.99
# MildlySuccesfull = greater than .25 to less than .50
# VeryLittleSucess = greater then .20 to .25
# Unsuccesfull = 0 points to .19
# BadPlay = less than 0

def createSuccesCategories(prev_down_val, yards_needed_val, yards_gained_val,
                           prev_play_val, what_happened_val, theList):
    ''' Method to make the categories for the type of previous play

        df: The dataframe that to be worked on.

        asScore:  Default is False.  When true will cause the scores used to
                  bin the previous plays to be returned as a list.

        addCatAsColumns:  Default is True. When True it will cause the categories
                          to be added to the dataFrame and then the whole dataFrame is
                          returned. When false will return a list that contains the categories
                          The first category is the worst and progressively getting better
                          and better to the end of the category list.

        Returns:    Will return list of Scores is asScore is True.  Will return list of
                    categorieys if addCatAsColumns is False.  Otherwise will return the new
                    dataframe with the categories added to it.
                    '''

    # This is the default score for the first play
    defaultScore = .65
    playQuality = [defaultScore]  # This is appended because we are looking at
    # the previous play.  The first play recieves this
    # score for a pretend previou play neither success nor
    # to much success.
    score = 0
    theScore = 0
    bins = [0, .20, .26, .51, 1.0, 2, 99]

    # This is the list that will contain the prev_plays_quality
    prev_play_quality = []

    catNamesRun = ['prev_ply_bad_run', 'prev_ply_no_succ_run', 'prev_ply_little_succ_run',
                   'prev_ply_mild_succ_run', 'prev_ply_somewhat_succ_run', 'prev_ply_succ_run',
                   'prev_ply_high_succ_run'
                   ]

    catNamesPass = ['prev_ply_bad_pass', 'prev_ply_no_succ_pass', 'prev_ply_little_succ_pass',
                    'prev_ply_mild_succ_pass', 'prev_ply_somewhat_succ_pass', 'prev_ply_succ_pass',
                    'prev_ply_high_succ_pass'
                    ]

    catListPass = [0, 0, 0, 0, 0, 0, 0]
    catListRun = [0, 0, 0, 0, 0, 0, 0]

    # except for the last play becuase this has
    # no play after it.

    # Filling in the categories

    score = 0

    down = prev_down_val
    # making the two point conversion act as a
    # fourth down
    if down == 5:
        down = 4

    percentage = getPercentage(down, yards_needed_val)

    theScore = (yards_gained_val / percentage)
    # Got enough yards here to
    # make a first down
    if theScore >= 1:
        score = 1
        if down == 4:
            score += 1

            # doing the fractional part
    else:
        score = theScore - (down / 10)
    # Adjusting the scores according to what happened on the
    # Play
    if what_happened_val == 'interception':
        score = score - 4
    if what_happened_val == 'fumble':
        score = score - 2
    if yards_gained_val >= 15:
        score = score + 1
    if what_happened_val == 'touchDown':
        score = score + 1
    # Getting the type of play that was done
    thePlayType = prev_play_val

    # making the score a float of 2 digits

    score = round(float(score), 3)

    # catList, theScore, theBins
    categoryList = loadBothCategories(catListRun, catListPass,
                                      score, thePlayType, bins, catNamesRun, catNamesPass)
    # Filling in the categories

    for i in range(len(categoryList)):
        theList.append(categoryList[i])

    return theList

    # End of the functions that are used to make the success categories



def makeformations(formation_val, theList):
  formations = ['Formation_NO HUDDLE SHOTGUN',
          'Formation_UNDER CENTER',
          'Formation_SHOTGUN',
          'Formation_NO HUDDLE',]
  for i in range(len(formations)):
    if formations[i] == formation_val:
      theList.append((formations[i], 1))
    else:
      theList.append((formations[i], 0))
  return theList


#'Own',  'value': 1},
#Opposing', 'value': 0},
def makeYardLine(yard_line_val, own_val):
  if own_val == 1:
    return yard_line_val
  else:
    theYards = yard_line_val
    theYardLine = 50 + (50 - theYards)
    return theYardLine


def fillTwoPoint(down_val):

    if down_val == 5:
        return 1
    else:
        return 0



@app.callback(Output("predHere", 'children'),
              [Input('predict_button', 'n_clicks')],
              [State('quarter', 'value'),
               State('yard_line', 'value'),
               State('formation', 'value'),
               State('minute', 'value'),
               State('seconds', 'value'),
               State('offense_score', 'value'),
               State('defense_score', 'value'),
               State('own_yard_line', 'value'),
               State('down', 'value'),
               State('yard_to_go', 'value'),
               State('show_proba', 'value'),



                State('prev_down', 'value'),
                State('yards_needed', 'value'),
                State('yards_gained', 'value'),
                State('prev_play', 'value'),
                State('what_happened', 'value'),

               ])

def update_output(n_clicks, quarter_val, yard_line_val, formation_val,
                   min_val, sec_val, your_score_val,
                  opp_score_val, own_val,
                  down_val, yard_to_go_val, proba_val,
                  prev_down_val, yards_needed_val, yards_gained_val,
                  prev_play_val, what_happened_val):
    # Will pass in the score, the current down the
    # yards to go for first down,
    # time in minutes and the time in seconds,
    # the quarter, yards gained on the previous play , type of play it was
    # what happened in the play, the formation of current play,

    if n_clicks is not None:
        # Checking to make sure that all the fields have
        # been entered
        if quarter_val is not None and  yard_line_val is not None and formation_val is not None  and \
                   min_val is not None and sec_val is not None and your_score_val is not None and \
                opp_score_val is not None and own_val is not None and \
                  down_val is not None and yard_to_go_val is not None and proba_val is not None and \
                  prev_down_val is not None and  yards_needed_val is not None and \
                yards_gained_val is not None and \
                  prev_play_val is not None and  what_happened_val is not None:

            # ['Quarter',
            #  'YardLine',
            #  'Formation_NO HUDDLE SHOTGUN',
            #  'Formation_UNDER CENTER',
            #  'Formation_SHOTGUN',
            #  'Formation_NO HUDDLE',
            #  'IsTwoPointConversion',
            #  'SecondsLeftInGame',
            #  'Score',
            #  'yards_gained_prev_off_play',
            #  'prev_offense_play_Pass',
            #  'prev_offense_play_Rush',
            #  'prev_offense_play_No Previous',
            #  'prev_ply_bad_run',
            #  'prev_ply_bad_pass',
            #  'prev_ply_no_succ_run',
            #  'prev_ply_no_succ_pass',
            #  'prev_ply_little_succ_pass',
            #  'prev_ply_mild_succ_run',
            #  'prev_ply_mild_succ_pass',
            #  'prev_ply_succ_run',
            #  'prev_ply_succ_pass',
            #  'prev_ply_high_succ_run',
            #  'prev_ply_high_succ_pass',
            #  'first_to_go',
            #  'second_to_go',
            #  'third_to_go',
            #  'fourth_to_go',
            #  'two_point_to_go']
            featureList = ['Quarter',
              'YardLine',
              'Formation_NO HUDDLE SHOTGUN',
              'Formation_UNDER CENTER',
              'Formation_SHOTGUN',
              'Formation_NO HUDDLE',
              'IsTwoPointConversion',
              'SecondsLeftInGame',
              'Score',
              'yards_gained_prev_off_play',
              'prev_offense_play_Pass',
              'prev_offense_play_Rush',
              'prev_offense_play_No Previous',
              'prev_ply_bad_run',
              'prev_ply_bad_pass',
              'prev_ply_no_succ_run',
              'prev_ply_no_succ_pass',
              'prev_ply_little_succ_run',
              'prev_ply_little_succ_pass',
              'prev_ply_mild_succ_run',
              'prev_ply_succ_run',
              'prev_ply_succ_pass',
              'prev_ply_high_succ_run',
              'prev_ply_high_succ_pass',
              'first_to_go',
              'second_to_go',
              'third_to_go',
              'fourth_to_go',
              'two_point_to_go']
            # creating the data for the prediction
            # putting everything in  a list of tuples
            theList = []

            theList.append((featureList[0], quarter_val))
            theList.append((featureList[1], makeYardLine(yard_line_val, own_val)))
            theList = makeformations(formation_val, theList)

            theList.append((featureList[6], fillTwoPoint(down_val)))
            theList.append((featureList[7], makeSecondsTillEnd(min_val, sec_val, quarter_val)))
            theList.append((featureList[8], your_score_val - opp_score_val))
            theList.append((featureList[9], yards_gained_val))
            theList = makePrevPlay(prev_play_val, theList)
            theList = createSuccesCategories(prev_down_val, yards_needed_val, yards_gained_val,
                                             prev_play_val, what_happened_val, theList)
            theList = makeDownCols(theList, down_val, yard_to_go_val)

            # now will build the dataFrame
            theData = pd.DataFrame(data=dict(theList), index=[0])
            # changing it to a numpy array
            theValues = theData

            choices = ['Pass', 'Rush']
            theIndex = 0
            thePred = ""
            theProbas = theXgb.predict_proba(theValues)

            if theProbas[0,0] > theProbas[0,1]:
                thePred = 'Pass'
            else:
                theIndex = 1
                thePred = "Run"

            # 0 means don't show the proba value
            if proba_val == 0:
                return f" \"{thePred}\" was predicted!"
            else:
                # getting the probability set up
                theProb = (theProbas[0,theIndex]) * 100
                return f" \"{thePred}\" was predicted with a probability of {theProb:.2f}%"

        else:
            return f"You need to make sure all fields are entered"
