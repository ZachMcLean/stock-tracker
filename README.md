# Stock Tracker App
This is a web-based Stock Tracker application built using Flask, Alpha Vantage API, and News API. The app allows users to track the stock prices of their favorite companies, view the latest stock-related news, and see real-time stock price updates. The daily prices are presented in a collapsible table, and the current stock price is dynamically updated every 10 minutes.

### Features
- Stock Tracking: Enter a stock symbol to get daily stock prices, including open, high, low, close, and volume data.
- Trending News: Get the latest news related to the entered stock symbol.
- Real-Time Price Updates: The current stock price is displayed and updated automatically every 10 minutes.
- Collapsible Daily Prices Table: The daily stock prices table can be expanded or collapsed for easier navigation.

### Prerequisites
- Python 3.6+
- Flask
- API keys for:
    - Alpha Vantage
    - News API

### Installation
1. Clone the Repository:
```bash
Copy code
git clone https://github.com/yourusername/stock-tracker-app.git
cd stock-tracker-app
```

2. Set Up a Virtual Environment:
```bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the Dependencies:
```bash
Copy code
pip install -r requirements.txt
```

4. Set Up Environment Variables:

- Create a .env file in the root directory of your project.
- Add your API keys to the .env file:
```bash
Copy code
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
NEWS_API_KEY=your_news_api_key
```

5. Run the Application:
```bash
Copy code
python app.py
```

6. Access the Application:
Open your web browser and navigate to http://127.0.0.1:5000/

### Usage
1. Track a Stock:

- Enter the stock symbol (e.g., AAPL for Apple) in the input field and click "Track."
- The app will display the current stock price and a chart of daily prices.
- The daily prices table is collapsible and can be expanded or collapsed by clicking on the "Daily Prices" header.

2. View Trending News:

- Below the stock data, the app shows a list of the latest news articles related to the entered stock symbol.

3. Real-Time Price Updates:

- The current stock price displayed at the top will automatically refresh every 10 minutes.

### File Structure
- app.py: The main Flask application file that handles routes and API requests.
- templates/: Contains the HTML templates for rendering the web pages (index.html, stock_detail.html).
- static/: Contains static files such as CSS (style.css) and JavaScript (script.js).
- README.md: This file, providing an overview and instructions for the app.

### Customization
- Update Interval: You can modify the frequency of the real-time price updates by changing the interval in the JavaScript code within index.html (default is 600000 milliseconds or 10 minutes).
- Styling: Customize the look and feel of the app by editing the style.css file in the static folder.

### Known Issues
- The Alpha Vantage API has a limit on the number of requests per minute. If you encounter issues with fetching data, consider upgrading your API plan or caching the results.

