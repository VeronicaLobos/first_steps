"""
Learning objectives:
- Understand how to use SQLAlchemy to connect to a SQLite database
- Learn how to execute SQL queries using SQLAlchemy
- Learn how to fetch and print results from a query

 * Exercise: Writing different queries

Try to change your code to execute the following query:
Print all the books from the table books where the publication
year is after 2000.
Print the same results as #1, but also print the number of
results retrieved (Returned 52 results).
Add another query that prints all the book names along with their
authors’ name, like that: Frankenstein (Mary Shelley). You should
print the books in Alphabetical order.
⭐ Hint: you need to JOIN the books and authors tables.
"""

from sqlalchemy import create_engine, text

# Create an engine that connects to a SQLite
# database file named "example.sqlite3"
engine = create_engine('sqlite:///data/textbook.sqlite3')

with engine.connect() as connection:
    # Run an SQL query
    query = '''
          SELECT books.title, authors.name
          FROM books
          JOIN authors
          ON books.author_id = authors.author_id
          WHERE publication_year > 2000
          ORDER BY authors.name
          ;
          '''

    results = connection.execute(text(query))
    rows = results.fetchall()

    # Print results
    num_rows = 0
    for title, name in rows:
        print(f'{title} ({name})')
        num_rows +=1
    print(f'Returned {num_rows} results.')
    # Close the connection
