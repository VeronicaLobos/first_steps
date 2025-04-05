"""
Object Relational Mapping (ORM) with SQLAlchemy

ORM is a programming technique that allows you to interact
with a database using Python objects instead of writing raw
SQL queries. SQLAlchemy is a popular ORM library for Python
that provides a high-level API for working with databases.

Learning to:
- ... use SQLAlchemy ORM to interact with a SQLite database
- ...define database models using SQLAlchemy ORM
- ... create a database session and perform CRUD operations
- ... query the database using SQLAlchemy ORM
- ... define relationships between tables using SQLAlchemy ORM
- ... use the declarative base class to define models
- ... use the sessionmaker class to create sessions

Functions used:
 - relationship(): defines relationships
 - back_populates() to define bidirectional relationships
 - create_all() to create tables
 - add_all() to add multiple objects to the session
 - commit() to save changes to the database
 - query() to query the database
 - all() to retrieve all results from a query
 - close() to close the session

With ORM + OOP, you can define:
- classes that represent database tables
- attributes of those classes represent table columns
- methods of those classes represent database operations
- and instances of those classes represent rows.

This allows you to work with
the database using Python objects and methods, rather
than writing raw SQL queries. This makes your code
more readable, maintainable, and easier to understand.

"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Define the database model
Base = declarative_base()

# Define the Book class
class Book(Base):
    # Define the table name and columns
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.author_id'))
    title = Column(String)
    publication_year = Column(Integer)
    # Define the relationship with the Author class
    author = relationship("Author", back_populates="books")

# Define the Author class
class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    name = Column(String)
    # Define the relationship with the Book class
    books = relationship("Book", back_populates="author")



# Create a database connection
engine = create_engine('sqlite:///books_db.sqlite3')
    # Create the database tables
Base.metadata.create_all(engine)
    # Create a session
Session = sessionmaker(bind=engine)
    # Create a session instance
session = Session()


### Perform database operations ###

# Create a new record for Book
book = Book(
    book_id = 1,
    author_id = 1,
    title = 'My Annihilation',
    publication_year = 2022
)

# Create a new record for Author
author = Author(
    author_id = 1,
    name = 'Fuminori Nakamura'
)

# Add and commit the session to save changes
session.add_all([book, author])
session.commit()


### Query the database
## Query all books

print("\n**** Books ****")
for book in session.query(Book).all():
    if book.author: # Join the author
        print(f'{book.title} ({book.publication_year}) by {book.author.name}')
    else:
        print(f'{book.title} ({book.publication_year})')

## Query all authors

print("\n**** Books by Author ****")
for author in session.query(Author).all():
    if author.books: # Join the books
        print(f'{author.name}:')
        for book in author.books:
            print(f' - {book.title} ({book.publication_year})')

session.close()
