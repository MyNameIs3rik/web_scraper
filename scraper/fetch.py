import time
from bs4 import BeautifulSoup
import requests

def fetch(url):
    result = requests.get(url)
    return BeautifulSoup(result.text, 'html.parser')

def parse(html):
    data = []
    books = html.find_all('article', class_='product_pod')
    for book in books:
        title = book.find('h3').find('a').get('title')
        price = book.find('p', class_='price_color').text.strip()[1:]
        stock = book.find('p', class_='instock availability').text.strip()
        rating = book.find('p', class_ = 'star-rating').get('class')[1]
        data.append({
            'title': title,
            'price': price,
            'stock': stock,
            'rating': rating
        })
    
    return data


if __name__ == "__main__":
    url = "https://books.toscrape.com/"
    data = parse(fetch(url))
    print(data)
