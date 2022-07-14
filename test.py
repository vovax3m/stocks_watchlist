import yfinance as yf
from flask import Flask , render_template, request
import datetime
app = Flask(__name__)
data={'TDOC': {'ask': 174.25, 'open': 170.93, 'high': 174.37, 'low': 168.51, 'pers': 4.4, 'diff': 7.35, 'pers_sort': 44}, 'ZM': {'ask': 182.5, 'open': 168, 'high': 179.99, 'low': 167.86, 'pers': 11.59, 'diff': 18.95, 'pers_sort': 116}, 'AAPL': {'ask': 319.05, 'open': 319.25, 'high': 321.15, 'low': 316.47, 'pers': 0.25, 'diff': 0.8, 'pers_sort': 3}, 'UBER': {'ask': 35.98, 'open': 34.18, 'high': 36.45, 'low': 34, 'pers': 5.36, 'diff': 1.83, 'pers_sort': 54}, 'W': {'ask': 172, 'open': 165.07, 'high': 177.28, 'low': 163.615, 'pers': 5.98, 'diff': 9.7, 'pers_sort': 60}, 'KSS': {'ask': 19.36, 'open': 19.54, 'high': 19.73, 'low': 18.8, 'pers': -3.78, 'diff': -0.76, 'pers_sort': -38}, 'SPXL': {'ask': 41.3, 'open': 39.88, 'high': 40.8414, 'low': 38.72, 'pers': 2.99, 'diff': 1.2, 'pers_sort': 30}, 'VNQ': {'ask': 78.99, 'open': 77.58, 'high': 78.14, 'low': 76.89, 'pers': 1.0, 'diff': 0.78, 'pers_sort': 10}, 'TSLA': {'ask': 842.75, 'open': 808.75, 'high': 834.4, 'low': 804.21, 'pers': 4.58, 'diff': 36.94, 'pers_sort': 46}, 'MSFT': {'ask': 183.88, 'open': 182.73, 'high': 184.27, 'low': 180.41, 'pers': 1.37, 'diff': 2.48, 'pers_sort': 14}, 'GOOG': {'ask': 1431.91, 'open': 1416.94, 'high': 1432.57, 'low': 1413.68, 'pers': 1.07, 'diff': 15.18, 'pers_sort': 11}, 'AMZN': {'ask': 2444, 'open': 2415.94, 'high': 2442.37, 'low': 2398.1973, 'pers': 1.79, 'diff': 42.9, 'pers_sort': 18}}
#list=['TDOC', "ZM", "AAPL", "UBER", "W","KSS", "SPXL", "VNQ","TSLA", "MSFT", "GOOG", "AMZN" ]
list =["ZM","W","UBER","TSLA", "TDOC","SPXL", "AMZN", "MSFT", "GOOG","VNQ", "AAPL", "KSS"]
#print(sorted(data,key={i['pers_sort'] for i in data.values()},reverse=True))

#v=sorted(data.items(), key=lambda k_v: k_v[1]['pers_sort'],reverse=True)
#print(v)



x=[('ZM', {'ask': 182.5, 'open': 168, 'high': 179.99, 'low': 167.86, 'pers': 11.59, 'diff': 18.95, 'pers_sort': 116}), ('W', {'ask': 172, 'open': 165.07, 'high': 177.28, 'low': 163.615, 'pers': 5.98, 'diff': 9.7, 'pers_sort': 60}), ('UBER', {'ask': 35.98, 'open': 34.18, 'high': 36.45, 'low': 34, 'pers': 5.36, 'diff': 1.83, 'pers_sort': 54}), ('TSLA', {'ask': 842.75, 'open': 808.75, 'high': 834.4, 'low': 804.21, 'pers': 4.58, 'diff': 36.94, 'pers_sort': 46}), ('TDOC', {'ask': 174.25, 'open': 170.93, 'high': 174.37, 'low': 168.51, 'pers': 4.4, 'diff': 7.35, 'pers_sort': 44}), ('SPXL', {'ask': 41.3, 'open': 39.88, 'high': 40.8414, 'low': 38.72, 'pers': 2.99, 'diff': 1.2, 'pers_sort': 30}), ('AMZN', {'ask': 2444, 'open': 2415.94, 'high': 2442.37, 'low': 2398.1973, 'pers': 1.79, 'diff': 42.9, 'pers_sort': 18}), ('MSFT', {'ask': 183.88, 'open': 182.73, 'high': 184.27, 'low': 180.41, 'pers': 1.37, 'diff': 2.48, 'pers_sort': 14}), ('GOOG', {'ask': 1431.91, 'open': 1416.94, 'high': 1432.57, 'low': 1413.68, 'pers': 1.07, 'diff': 15.18, 'pers_sort': 11}), ('VNQ', {'ask': 78.99, 'open': 77.58, 'high': 78.14, 'low': 76.89, 'pers': 1.0, 'diff': 0.78, 'pers_sort': 10}), ('AAPL', {'ask': 319.05, 'open': 319.25, 'high': 321.15, 'low': 316.47, 'pers': 0.25, 'diff': 0.8, 'pers_sort': 3}), ('KSS', {'ask': 19.36, 'open': 19.54, 'high': 19.73, 'low': 18.8, 'pers': -3.78, 'diff': -0.76, 'pers_sort': -38})]


#for i in x:
#    print(f"key={i[0]},dict={i[1]['ask']}")

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
    """convert a datetime to a different format."""
    return value.strftime(format)

app.jinja_env.filters['datetimefilter'] = datetimefilter
@app.route("/")
def index():
    return render_template('table.html', tickers=" ".join(list),data=x,current_time=datetime.datetime.now())         

if __name__ == '__main__':
    app.run(debug=False) 