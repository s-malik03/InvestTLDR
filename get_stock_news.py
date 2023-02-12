import requests
import bs4
import json

def stock_news(ticker, sort="entity_match_score", text={}):

    url = "https://api.marketaux.com/v1/news/all"
    params = {"api_token": "CgFM2nerQUYMiBIMHSnM9TmA6tRgFCn1aZFvhcQU", "sort":sort, "symbols":ticker}

    response = requests.get(url, params=params)
    data = response.json()

    for item in data["data"]:
        html = requests.get(item["url"]).text
        soup = bs4.BeautifulSoup(html, "html.parser")
        text[item["title"]] = soup.get_text()

    print(json.dumps(text))

    return text



