import sqlite3
from pathlib import Path

from scraper.fetch import fetch
from processing.clean import clean_data

DB_PATH = Path("books.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables(conn):
    with open("db/schema.sql", "r", encoding="utf-8") as f:
        conn.executescript(f.read())



def insert_books(conn, books: list[dict]):
    query = """
    INSERT INTO books (title, price, in_stock, rating)
    VALUES (?, ?, ?, ?)
    """

    rows = [
        (
            book["title"],
            book["price"],
            book["stock"],
            book["rating"],
        )
        for book in books
    ]

    conn.executemany(query, rows)

def pipline():
    raw_books = fetch("https://books.toscrape.com/")
    cleaned_books = clean_data(raw_books)

    conn = get_connection()
    create_tables(conn)
    insert_books(conn, cleaned_books)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    pipline()