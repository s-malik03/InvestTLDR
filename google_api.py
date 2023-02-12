import requests

def get_top_ten_google_news_results(query):
    api_key = '2ad16076d8334e1bb196146e75bc3a2a'
    query = query.replace(' ', '%20')
    url = f'https://newsapi.org/v2/top-headlines?category=business&apiKey=2ad16076d8334e1bb196146e75bc3a2a&q={query}'
    response = requests.get(url)
    print(response.text)
    response_json = response.json()
    return response_json['articles'][:10]

if __name__ == '__main__':
    query = input('Enter your search query: ')
    results = get_top_ten_google_news_results(query)
    for i, result in enumerate(results):
        print(f'{i+1}. {result["url"]}')

