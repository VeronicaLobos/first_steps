"""
💪 Exercise

* Add 35 books to the static list you created in the
 Flask app in Codio (it can be fake books, or the same books).
* Run the Flask app from Codio.
* Write a script, on your computer, that interacts with Codio’s
 Flask endpoint and reads 5 books at a time, until all the
 books are read.
 To clarify, your code on your computer needs to communicate
 with the API, in a loop, and read 5 books at a time.
 The code will loop until all the books are fetched.
"""

import requests as req

URL = "https://diegogarage-cameraalamo-5000.codio.io/api/books"

def get_books(pages, limit):
    print("------ Books API ------")
    for page in range(1, pages + 1):
        payload = {"page": page, "limit": limit}
        response = req.get(URL, params=payload)
        response.raise_for_status()
        books = response.json()
        print(f"\n--- Page {page} ---")
        for book in books:
            print(f"{book.get('id')}. \"{book.get('title')}\" "
                  f"by {book.get('author')}")

get_books(7, 5)
