import requests
from bs4 import BeautifulSoup

def get_news_articles(company):
    query = company
    query = query.replace(' ', '+')
    url = f'https://www.google.com/search?q={query}&tbm=nws'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.select('.r a')
    return [link.get('href') for link in links]

if __name__ == '__main__':
    company = input('Enter company name: ')
    urls = get_news_articles(company)
    for i, url in enumerate(urls):
        print(f'{i+1}. {url}')

