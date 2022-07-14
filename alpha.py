
import requests

symbol="AAPL"
apikey="apikey"
url=f"https://www.alphavantage.co/query?datatype=csv&function=GLOBAL_QUOTE&symbol={symbol}&apikey={apikey}"
data={}
try:
    x = requests.get(url1)
except Exception as err:
    print(f"failed with: {err}")
else:      
    lines = x.text.split("\n")
    for idx, line in enumerate(lines):
        if idx == 0 or len(line) == 0:
             continue
        words= line.split(",")
        if len(words) > 0:
            data['symbol']=words[0]
            data['open']=words[1]
            data['high']=words[2]
            data['low']=words[3]
            data['price']=words[4]
            data['volume']=words[5]
            data['latestDay']=words[6]
            data['previousClose']=words[7]
            data['change']=words[8]
            data['changePercent']=words[9].replace("\r","")
print(data)
        