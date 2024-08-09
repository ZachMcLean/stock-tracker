from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API keys (Replace these with your own keys)
ALPHA_VANTAGE_API_KEY = 'TTM4JQD169JD59WR'
NEWS_API_KEY = '1b7e0cec090548fdacc2d8cb7c46c963'

# API endpoints
ALPHA_VANTAGE_URL = 'https://www.alphavantage.co/query'
NEWS_API_URL = 'https://newsapi.org/v2/everything'

@app.route('/', methods=['GET', 'POST'])
def index():
    stock_data = None
    news_data = None
    symbol = None

    if request.method == 'POST':
        symbol = request.form.get('symbol')
        if symbol:
            # Fetch stock prices
            stock_params = {
                'function': 'TIME_SERIES_DAILY',
                'symbol': symbol,
                'apikey': ALPHA_VANTAGE_API_KEY
            }
            stock_response = requests.get(ALPHA_VANTAGE_URL, params=stock_params)
            if stock_response.status_code == 200:
                stock_data = stock_response.json().get('Time Series (Daily)', {})

            # Fetch trending news
            news_params = {
                'apiKey': NEWS_API_KEY,
                'q': symbol,
                'language': 'en',
                'sortBy': 'publishedAt'
            }
            news_response = requests.get(NEWS_API_URL, params=news_params)
            if news_response.status_code == 200:
                news_data = news_response.json().get('articles', [])

    return render_template('index.html', stock_data=stock_data, news_data=news_data, symbol=symbol)

@app.route('/stock/<symbol>')
def stock_detail(symbol):
    # Fetch detailed stock data and financial metrics
    stock_params = {
        'function': 'OVERVIEW',
        'symbol': symbol,
        'apikey': ALPHA_VANTAGE_API_KEY
    }
    stock_response = requests.get(ALPHA_VANTAGE_URL, params=stock_params)
    stock_data = stock_response.json()

    return render_template('stock_detail.html', stock_data=stock_data, symbol=symbol)

if __name__ == '__main__':
    app.run(debug=True)

