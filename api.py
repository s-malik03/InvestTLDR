from flask import Flask
import get_stock_news as gsn
import inquire
import json
import yahooquery as yf
import requests
import bing_api
import bs4
from sec_cik_mapper import StockMapper

def fetch_10k_report(ticker):
    # Define the base URL for EDGAR search
    cik = StockMapper().ticker_to_cik[ticker.upper()]
    base_url = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={}&type=10-K&dateb=&owner=exclude&start=0&count=40&output=atom"

    # Replace the placeholder in the URL with the actual ticker
    url = base_url.format(cik)

    if ticker == "aapl":

        url = "https://www.sec.gov/Archives/edgar/data/320193/000032019318000145/a10-k20189292018.htm"

    # Send a GET request to the URL and store the response
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # The request was successful, parse the response as XML
        content = response.text
        # Return the content
        return content
    else:
        # The request was not successful, return an error message
        return "Failed to fetch 10-K report for ticker {}".format(ticker)


app = Flask(__name__)

@app.route('/analysis/<ticker>')

def analysis(ticker):

    ticker = ticker.lower()

    print(ticker)

    company = yf.Ticker(ticker).price[ticker]['shortName']

    print(company)

    data = {}

    urls = bing_api.get_news_articles(ticker)

    print("get url")

    for url in urls:

        print(f"get {url} of {len(urls)}")

        try:

            html = requests.get(url, timeout=10).text
            soup = bs4.BeautifulSoup(html, "html.parser")
            data[url] = soup.get_text()

        except:

            pass

    data["10k"] = bs4.BeautifulSoup(fetch_10k_report(ticker)).get_text()

    print("urls added") 


    """urls = bing_api.get_news_articles(company)

    print("get url 2")

    for url in urls:

        html = requests.get(url).text
        soup = bs4.BeautifulSoup(html, "html.parser")
        data[url] = soup.get_text()

    print("get url 3")"""

    url = "https://inquire.maheshnatamai.com"

    key = "8ZC8lvc9IBCZQb4jj-O9Uw"

    with open(f"{ticker}.json", 'w') as file:

        file.write(json.dumps(data))

    inquire.create_collection(url, ticker, ticker+".json", key)

    print("create collection")

    response = inquire.ask_collection(url, ticker, f"Should I invest in {company}? Yes or no. Give reasons why.", key)

    print("ask")

    inquire.delete_collection(url, ticker, key)

    print("delete")

    response = response.json()

    response["10k"] = data["10k"]

    response["urls"] = urls

    return json.dumps(response)

    
