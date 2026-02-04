import sqlite3

conn = sqlite3.connect("books.db")
cursor = conn.cursor()

cursor.execute("""
    SELECT title, price, rating
    FROM books
    WHERE rating >= 4
      AND in_stock = 1
    ORDER BY price ASC
    LIMIT 20
""")

for book in cursor.fetchall():
    print(book[0] + ",", "$" + str(book[1]),"Rating:", book[2])
