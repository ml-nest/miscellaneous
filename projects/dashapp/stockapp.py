## Importing Packages
import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly 
import random 
import plotly.graph_objs as go 
from plotly.subplots import make_subplots
from collections import deque 
import datetime

# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Purchased Stock Quotes", style={'text-align': 'center'}),

    dcc.Dropdown(id="stock_quote",
                 options=[
                     {"label": "Reliance", "value": 'RELIANCE'},
                     {"label": "HDFC", "value": 'HDFC'},
                     {"label": "ONGC", "value": 'ONGC'},
                     {"label": "IRFC", "value": 'IRFC'},
                     {"label": "JKTYRE", "value": 'JKTYRE'}
                     ],
                 multi=False,
                 value='RELIANCE',
                 style={'width': "40%"}
                 ),
    dcc.Input(id="days", type="number", placeholder="Input number of days", value=100),
    dcc.Input(id="freq", type="number", placeholder="Frequency", value=1),
    dcc.Dropdown(id="time",
                 options=[
                     {"label": "Min", "value": 'm'},
                     {"label": "Day", "value": 'd'},
                     {"label": "Week", "value": 'wk'},
                     {"label": "Month", "value": 'mo'},],
                 multi=False,
                 value='d',
                 style={'width': "40%"}
                 ),
    html.Br(),

    dcc.Graph(id = 'live-graph', animate = True), 
    dcc.Interval(
        id = 'graph-update', 
        interval = 1000, 
        n_intervals = 0
        )

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(component_id='live-graph', component_property='figure'),
    [Input(component_id='stock_quote', component_property='value'),
    Input('graph-update', 'n_intervals'),
    Input('days', "value"),
    Input('freq', "value"),
    Input(component_id='time', component_property='value') ]
)
def update_graph(ticker, n, days, freq, time):
    print(ticker, n, days, freq, time)
    stockdata = yf.download(tickers=ticker+'.NS', period=str(days)+'d', interval=str(freq)+time)
    stockdata.head(2)
    fig = go.Figure()

    #Candlestick
    fig.add_trace(go.Candlestick(x=stockdata.index,
                    open=stockdata['Open'],
                    high=stockdata['High'],
                    low=stockdata['Low'],
                    close=stockdata['Close'], name = 'market data'))

    # Add titles
    fig.update_layout(yaxis_title='Stock Price (Rupee per Share)')
    fig.update_layout(xaxis=dict(range=[min(stockdata.index),max(stockdata.index)]),
    yaxis = dict(range = [0.99*min(stockdata['Low']),1.01*max(stockdata['High'])]), height=700)


    return fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)