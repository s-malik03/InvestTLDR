import requests
import json
import bs4

def get_news_articles(company):
    query = f'"{company}"'
    headers = {
        'Ocp-Apim-Subscription-Key': 'afb43b53c95e45f38abaed82fd388bf7'
    }
    params = {
        'q': query,
        'count': 10,
        'mkt': 'en-US'
    }
    url = 'https://api.bing.microsoft.com/v7.0/news/search/'
    print(company)
    response = requests.get(url, headers=headers, params=params)
    print("Bing search completed")
    response_json = response.json()
    articles = response_json['value']
    return [article['url'] for article in articles]

if __name__ == '__main__':
    api_key = 'YOUR_API_KEY'
    company = input('Enter company name: ')
    urls = get_news_articles(company, api_key)
    for i, url in enumerate(urls):
        print(f'{i+1}. {url}')
