#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plotly
import dash
import dash_core_components as dcc
import dash_html_components as html
# import plotly.graph_objects as go
import plotly.express as px
from skimage import io
from dash.dependencies import Input, Output
import numpy as np
# from osgeo import gdal

# debug info
print('plotly=', plotly.__version__)
print('dash=', dash.__version__)
print('dash_html_components=', html.__version__)
print('dash_core_components=', dcc.__version__)

# application setup
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__)
colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}
app.layout = html.Div(children=[
    # plot title
    html.H1(children='Kilauea Spectral Map',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }),
    # plot subtitle
    html.P(children='''
        Analysis by Paul Giesting, using scikit-learn and LANDSAT 8 bands 1-7, 
        Analysis Ready Data tile HI004002, collected 4 February 2017.
        ''',
        style={
            'textAlign': 'center',
            #'color': colors['text']
        }
    ),
    # credit
    html.P(children='Powered by Plotly Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    # left side figure
    html.Div(children=[
        html.H3(id='lefttitle',style={'textAlign':'center'}),
        dcc.Graph(
            id='leftgraph'
        ),
        html.Label('Map Selection'),
        dcc.RadioItems(
            id='leftbutton',
            options=[
                {'label': 'True Color', 'value': 'tc'},
                {'label': 'False Color NIR', 'value': 'veg'},
                {'label': 'False Color SWIR', 'value': 'heat'},
                {'label': 'Principal Components', 'value': 'pca'}
            ],
            value='tc'
        ),
    ],
        style={'width':'49%','display':'inline-block'}
    ),
    # right side figure
    html.Div(children=[
        html.H3(id='righttitle',style={'textAlign':'center'}),
        dcc.Graph(
            id='rightgraph'
        ),
        html.Label('Map Selection'),
        dcc.RadioItems(
            id='rightbutton',
            options=[
                {'label': 'True Color', 'value': 'tc'},
                {'label': 'False Color NIR', 'value': 'veg'},
                {'label': 'False Color SWIR', 'value': 'heat'},
                {'label': 'Principal Components', 'value': 'pca'}
            ],
            value='pca'
        ),
    ],
        style={'width':'49%','display':'inline-block'}
    ),
])

# figure loading
figdict = {'tc':'tccrop.jpg','pca':'pccrop.jpg','veg':'vfccrop.jpg','heat':'hfccrop.jpg'}
figpath = 'assets/images/'
titledict = {
    'tc':'True Color',
    'pca':'Spectral Principal Components',
    'veg':'Near Infrared (Vegetation=Red)',
    'heat':'Shortwave Infrared'
    }

@app.callback(
    [Output('leftgraph', 'figure'),
     Output('lefttitle', 'children')],
    [Input('leftbutton', 'value')]
    )
def update_left_figure(button):
    array = io.imread(figpath+figdict[button])
    fig = px.imshow(array)
    fig.update_layout(width=780, height=900, margin={'l':5,'r':5,'b':5,'t':5})
    return fig, titledict[button]

@app.callback(
    [Output('rightgraph', 'figure'),
     Output('righttitle', 'children')],
    [Input('rightbutton', 'value')]
    )
def update_right_figure(button):
    array = io.imread(figpath+figdict[button])
    fig = px.imshow(array)
    fig.update_layout(width=780, height=900, margin={'l':5,'r':5,'b':5,'t':5})
    return fig, titledict[button]

if __name__ == '__main__':
    app.run_server(debug=True)