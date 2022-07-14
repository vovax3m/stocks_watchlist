#!/bin/python3

from flask import Flask, render_template, request
import requests
import datetime
import json

app = Flask(__name__)

#stocks list
tickerlist = [
    'FB'
    'AMZN'
    'AAPL',
    'NFLX'
    'GOOG',
    'TSLA',
    'MSFT'
]
data={}


def yfinance(t):
    """ source of financial information per ticker """
    import yfinance as yf

    try:
        ticker = yf.Ticker(t)
    except Exception as err:

        print(f"failed with: {err}")
        return("Failed", status.HTTP_503_SERVICE_UNAVAILABLE)

    else:
        data["symbol"] = t
        data["price"   = ticker.info['ask']
        data["open"]   = ticker.info['open']
        data["high"]   = ticker.info['dayHigh']
        data["low"]    = ticker.info['dayLow']
        data["previousClose"] = ticker.info['previousClose']
        data['change'] = round( data["price"]  - data["previousClose"], 2 )
        data['changePercent'] = round(( data["price"]  - data["previousClose"]) / data["previousClose"] * 100, 2 )

    return data

def finnhub(t):
    """ another source of financial information per ticker """
    apikey="apikey_here"
    url=f"https://finnhub.io/api/v1/quote?symbol={t}&token={apikey}"

    try:
        response = requests.get(url)
        info = response.json()
        if len( info ) == 0:
            raise ValueError

    except Exception as err:

        print(f"Failed with: {err}")
        return("Failed", status.HTTP_503_SERVICE_UNAVAILABLE)

    else:
        data['symbol'] = t
        data['open']   = info['o']
        data['high']   = info['h']
        data['low']    = info['l']
        data['price']  = info['c']
        data['previousClose'] = info['pc']
        data['change'] = round( info['c'] - info['pc'], 2 )
        data['changePercent'] = round(( info['c'] - info['pc']) / info['pc'] * 100, 2 )
    return data
    
def getdata( ticker = None ):
    """ get data from provider """
    tickerdatamap = {}
    resultmap = {}
    if ticker:
        tickerdatamap = finnhub( ticker )
        resultmap.append[ tickerdatamap ]
    else:
        for ticker in tickerlist:
            provider = "finnhub"
            tickerdatamap = finnhub( ticker )
            if tickerdatamap == "Failed":
                print( f"{provider} failed" )
                tickerdatamap = yfinance( ticker )
            if isinstance( tickerdatamap, ( dict )):
                resultmap[ ticker ] = eval( str( tickerdatamap ))
    return(resultmap)

@app.template_filter()
def datetimefilter( value, format='%Y/%m/%d %H:%M' ):
    """convert a datetime to a different format."""
    return value.strftime(format)

@app.template_filter()
def str_to_obj( str ):
    return eval( str )
    
@app.route("/")
def index():
    return render_template(
        'table.html',
        tickers = " ".join( tickerlist ),
        data = getdata(),
        current_time = datetime.datetime.now()
    )

@app.route("/get")
def gettime():
    ticker = request.args.get( 'ticker' )
    tickerdata = finnhub( ticker )
    return(json.dumps( tickerdata ))

@app.route("/yf")
def yf():
    ticker = request.args.get('ticker')
    tickerdata = yfinance( ticker )
    return f"{tickerdata}"
    
@app.route("/getall")
def getall():
    alldata = getdata()
    return f"{ str( alldata ) }"
    
app.jinja_env.filters['datetimefilter'] = datetimefilter
app.jinja_env.filters['str_to_obj'] = str_to_obj

if __name__ == '__main__':
    app.run( debug = False )
