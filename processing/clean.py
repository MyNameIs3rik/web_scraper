def clean_price(price):
    if price is None:
        return None
    currency = ['$', '£', '€']
    for symbol in currency:
        price = price.replace(symbol, '')
    return float(price.strip())

def clean_stock(stock):
    if stock is None:
        return False
    if stock.lower().strip() == 'in stock':
        return True
    return False

def clean_rating(rating):
    ratings_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    return ratings_map.get(rating, 0)

def clean_title(title):
    if title is None:
        return ''
    title = title.replace('"', '')
    return title.strip()


def clean_book(book):
    return {
        'title': clean_title(book['title']),
        'price': clean_price(book['price']),
        'stock': clean_stock(book['stock']),
        'rating': clean_rating(book['rating'])
    }

def clean_data(data):
    return [clean_book(book) for book in data]

if __name__ == "__main__":
    pass