import pandas as pd

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv("Urban_Park_Ranger_Animal_Condition_Response.csv")

# you need to include __name__ in your Dash constructor if
# you plan to use a custom CSS or JavaScript in your Dash apps
app = dash.Dash(__name__)

#---------------------------------------------------------------
app.layout = html.Div([
    html.Div([
        html.Label(['NYC Calls for Animal Rescue']),  # label of drop down
        dcc.Dropdown(
            id='my_dropdown',   # name of dropdown
            options=[  # giving the label and the values that are related in the dataframe
                     {'label': 'Action Taken by Ranger', 'value': 'Final Ranger Action'},
                     {'label': 'Age', 'value': 'Age'},
                     {'label': 'Animal Health', 'value': 'Animal Condition'},
                     {'label': 'Borough', 'value': 'Borough'},
                     {'label': 'Species', 'value': 'Animal Class'},
                     {'label': 'Species Status', 'value': 'Species Status'}
            ],
            value='Animal Class',  # default value
            multi=False,   # multi drop down
            clearable=False,   # always have a value
            style={"width": "50%"}  # size of drop down
        ),
    ]),

    html.Div([
        dcc.Graph(id='the_graph')  # telling dash that we have a graph here with this name
    ]),

])

#---------------------------------------------------------------
@app.callback(
    Output(component_id='the_graph', component_property='figure'),   # connecting graph and components
    [Input(component_id='my_dropdown', component_property='value')]   # input is dropdown and graph is output
)

def update_graph(my_dropdown):
    dff = df   # always make a copy of main dataframe

    piechart=px.pie(
            data_frame=dff,
            names=my_dropdown,
            hole=.3,
            )

    return (piechart)


if __name__ == '__main__':
    app.run_server(debug=True)
