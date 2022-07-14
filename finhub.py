import requests
apikey="apikey"
t="TSLA"
url=f"https://finnhub.io/api/v1/quote?symbol={t}&token={apikey}"
data={}
try:
    x = requests.get(url)
except Exception as err:
    print(f"failed with: {err}")
else:    
    info=x.json()
    
    change = round(info['c'] - info['pc'],2)
    pers = round((info['c'] - info['pc']) /info['pc'] *100,4)    
    print(f"price:{info['c']}, chg:{change}, {pers}%")