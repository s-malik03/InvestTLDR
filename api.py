from flask import Flask
import get_stock_news as gsn
import inquire
import json
import yahooquery as yf
import requests

app = Flask(__name__)

@app.route('/analysis/<ticker>')

def analysis(ticker):

    ticker = ticker.lower()

    print(ticker)

    company = yf.Ticker(ticker).price[ticker]['longName']

    print(company)

    data = {}

    gsn.stock_news(ticker, text=data)

    gsn.stock_news(ticker, sort="published_on", text=data)

    url = "https://inquire.maheshnatamai.com"

    key = "8ZC8lvc9IBCZQb4jj-O9Uw"

    with open(f"{ticker}.json", 'w') as file:

        file.write(json.dumps(data))

    inquire.create_collection(url, ticker, ticker+".json", key)

    response = inquire.ask_collection(url, ticker, f"Should I invest in {company}? Yes or no. Give reasons why.", key)

    inquire.delete_collection(url, ticker, key)

    return response.text

    
