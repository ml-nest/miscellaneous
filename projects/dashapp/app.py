import dash 
from dash.dependencies import Output, Input
import dash_core_components as dcc 
import dash_html_components as html 
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
  
app.layout = html.Div( 
    [ 
        dcc.Graph(id = 'live-graph', animate = True), 
        dcc.Interval( 
            id = 'graph-update', 
            interval = 1000, 
            n_intervals = 0
        ), 
    ] 
) 
  
@app.callback( 
    Output('live-graph', 'figure'), 
    [ Input('graph-update', 'n_intervals') ] 
) 
  
def update_graph_scatter(n): 
    # X.append(X[-1]+1) 
    # Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))
    stockdata = yf.download(tickers='RELIANCE.NS', period='1h', interval='1m')
    fig = go.Figure()
    # fig = make_subplots()
    # fig.add_trace(
    #         go.Scattergl(
    #                 x = stockdata.index,
    #                 y = stockdata['Close'],mode="markers+lines", # marker_symbol="star",
    #     name='Close'
    #         ))

    # fig.add_trace(
    #         go.Scattergl(
    #                 x = stockdata.index,
    #                 y = stockdata['Open'],mode="markers+lines", # marker_symbol="star",
    #     name='Open'
    #         ))

    # fig.update_yaxes(title_text="Price", secondary_y=False)
    # fig.update_xaxes(title_text="Date")

    #Candlestick
    fig.add_trace(go.Candlestick(x=stockdata.index,
                    open=stockdata['Open'],
                    high=stockdata['High'],
                    low=stockdata['Low'],
                    close=stockdata['Close'], name = 'market data'))

    # Add titles
    fig.update_layout(
        title='BTC-INR',
        yaxis_title='Stock Price (Rupee per Share)')
    fig.update_layout(xaxis=dict(range=[min(stockdata.index),max(stockdata.index)]),yaxis = dict(range = [min(stockdata['Low']),max(stockdata['High'])]),title_text="Customizing Subplot Axes", height=700)

    return fig
  
    # data = plotly.graph_objs.Scatter( 
    #         x=stockdata.index, 
    #         y=stockdata['Close'], 
    #         name='Scatter', 
    #         mode= 'lines+markers'
    # ) 
  
    # return {'data': [data], 
            # 'layout' : go.Layout(xaxis=dict(range=[min(stockdata.index),max(stockdata.index)]),yaxis = dict(range = [min(stockdata['Close']),max(stockdata['Close'])]),)} 
  
if __name__ == '__main__': 
    app.run_server()