import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objs as go

symbol = '^NSEBANK'
ticker = yf.Ticker(symbol)
df = ticker.history(period='1d', interval='1m')

fig = go.Figure()

fig.add_trace(go.Candlestick(x=df.index,
                             open=df['Open'],
                             high=df['High'],
                             low=df['Low'],
                             close=df['Close'], name='market data'))

fig.update_layout(
    title = 'NSEBANK Live',
    xaxis_title = 'Time',
    yaxis_title = 'Price (in RS)',
    font=dict(
        color='White')
)

fig.update_layout({
    'paper_bgcolor': 'black'
})

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="minute", stepmode="backward"),
            dict(count=2, label="2m", step="minute", stepmode="backward"),
            dict(count=5, label="5m", step="minute", stepmode="backward"),
            dict(count=10, label="10m", step="minute", stepmode="backward"),
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=30, label="30m", step="minute", stepmode="backward"),
            dict(count=1, label="1h", step="hour", stepmode="backward"),
            dict(count=2, label="2h", step="hour", stepmode="backward"),
            dict(step="all")
        ]),
        font=dict(color='black')
    )
)

fig.show()













