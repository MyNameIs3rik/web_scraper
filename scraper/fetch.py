import time
from bs4 import BeautifulSoup
import requests

def fetch_page(url):
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

def fetch(url):
    html = fetch_page(url)
    pages = html.find('li', class_='current').text.strip()
    total_pages = int(pages.split()[-1])
    data = []
    for i in range(1, total_pages + 1):
        time.sleep(1)
        next_page_url = f"{url}catalogue/page-{i}.html"
        next_page_html = fetch_page(next_page_url)
        data += parse(next_page_html)
    return data


if __name__ == "__main__":
    url = "https://books.toscrape.com/"
    data = fetch(url)
    print(data)
