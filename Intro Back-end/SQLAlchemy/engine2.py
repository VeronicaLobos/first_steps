"""
Learning objectives:
- Understand how to use SQLAlchemy to connect to a SQLite database
- Learn how to execute SQL queries using SQLAlchemy
- Learn how to fetch and print results from a query
- Learn how to use Parameterized Queries to prevent SQL Injection
by escaping user input and using placeholders in SQL statements.

✍️ Exercise: Custom Search
Create a new script inside step2.py that will:
Ask the user to input a year.
Show all the books from this year.
Make sure your code is SQL Injection safe,
by implementing Parameterized Queries (You can test
it using the classic " OR 1=1-- injection).
"""


from sqlalchemy import create_engine, text

while True:
  search_input = input("Enter a publication year for the books catalog: ")
  try:
    year = int(search_input)
    if len(str(year)) == 4 and year < 2026:
      break
    else:
      print("Please, input a valid year")
  except ValueError:
    print("Please, input a 4 digit integer with a valid year")
    continue

params = {"search": search_input}

engine = create_engine('sqlite:///data/textbook.sqlite3')

with engine.connect() as connection:
    query = '''
          SELECT books.title, authors.name
          FROM books
          JOIN authors
          ON books.author_id = authors.author_id
          WHERE publication_year = :search
          ORDER BY books.title
          ;
          '''

    results = connection.execute(text(query), params)
    rows = results.fetchall()

    num_rows = 0
    print(f'Books published in {params["search"]}:')
    for title, name in rows:
        print(f'- {title} ({name})')
        num_rows +=1
    print(f'Returned {num_rows} results.')
