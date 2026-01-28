from scraper.fetch import fetch
from processing.clean import clean_data
import pandas as pd

def save_to_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('books_data.csv', index=False)

if __name__ == "__main__":
    url = "https://books.toscrape.com/"
    raw_data = fetch(url)
    cleaned_data = clean_data(raw_data)
    save_to_csv(cleaned_data)