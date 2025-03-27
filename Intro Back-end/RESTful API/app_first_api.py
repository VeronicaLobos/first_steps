"""
This module defines a Flask application that serves
as a RESTful API for managing a collection of books.

It provides endpoints for:
    - Retrieving books (with optional filtering and
     pagination).
    - Adding new books.
    - Updating existing books.
    - Deleting books.

The application uses a JSON file as a simple database and includes:
    - Error handling.
    - Rate limiting.
    - Logging: The application logs informational messages about incoming requests and other relevant events.
      The logs are configured to include timestamps, log levels, and messages, and are outputted to the console.
"""

import logging
from flask import Flask, jsonify, request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import json
import os
import webbrowser
from handle_json import HandleJson

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
limiter = Limiter(app=app, key_func=get_remote_address)


##  Data Validation

def validate_book_data(data: dict) -> bool:
    """
    Validates the book data to ensure it contains required fields.

    Receives a dictionary containing the book data.
    Returns True if the data is valid, False otherwise.
    """
    if "title" not in data or "author" not in data:
        return False
    return True


def _jsonify_tilde(filtered_books: list) -> Response:
    """
    A utility function that substitutes jsonify()
    when the database contains non-ASCII characters
    (in absence of client side code).

    Receives a list of book dictionaries.
    Returns a Flask Response object containing the
    JSON data with UTF-8 encoding.
    """
    json_str = json.dumps(filtered_books, ensure_ascii=False, indent=4)
    return Response(json_str, mimetype='application/json; charset=utf-8')


## API routes

@app.route('/api/books', methods=['GET', 'POST'])
@limiter.limit("10/minute")
def handle_books() -> Response:
    """
    Handles GET and POST requests for the /api/books
    endpoint.

    If the request is POST, it adds a new book to
    the database.
    If the request is GET, it retrieves books, optionally
    filtering by author or paginating.

    Returns a Flask Response object.
    """
    # Log a message
    app.logger.info('GET request received for /api/books')

    if request.method == 'POST':
        # Get the new book data from the client
        new_book = request.get_json()
        if not validate_book_data(new_book):
            return jsonify({"error": "Invalid book data"}), 400

        # Generate a new ID for the book
        new_id = max(book['id'] for book in books) + 1
        new_book['id'] = new_id

        # Add the new book to our list
        books.append(new_book)

        # Return the new book data to the client
        return jsonify(new_book), 201

    elif request.method == 'GET':
        author = request.args.get('author')
        if author:
            filtered_books = [book for book in books if book.get('author') == author]
            if not filtered_books:
                return jsonify({"error": "No books found for the given author"}), 404
            return _jsonify_tilde(filtered_books)

        else:
            page = int(request.args.get('page', 1))
            limit = int(request.args.get('limit', 5))

            start_index = (page - 1) * limit
            end_index = start_index + limit

            paginated_books = books[start_index:end_index]

            return _jsonify_tilde(paginated_books)


def _find_book_by_id(book_id: int) -> dict:
  """
  Receives an integer representing a book ID.

  Finds and returns the book dictionary with
  the corresponding id in the list of books.

  If there is no book with this id, return None.
  """
  book = [book for book in books if book['id'] == book_id]
  if len(book) == 0:
    return None
  return book[0]


@app.route('/api/books/<int:book_id>', methods=['PUT'])
def handle_book(book_id: int) -> Response:
    """
    Handles PUT requests for the /api/books/<id>
    endpoint to update a book.

    Receives an integer representing a book ID.

    Updates the database with the new data.

    Returns a Flask Response object containing the
    JSON data with UTF-8 encoding, with the updated
    book data... or an error message.
    """
    # Find the book with the given ID
    book = _find_book_by_id(book_id)

    # If the book wasn't found, return a 404 error
    if book is None:
        return '', 404

    # Update the book with the new data from the client
    new_data = request.get_json()
    book.update(new_data)

    # Update the database
    database.save_posts_to_json(books)

    # Return the updated book
    return _jsonify_tilde(book)


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Handles DELETE requests for the /api/books/<id>
    endpoint to delete a book.

    Receives an integer representing a book ID.

    Removes the book from the database.

    Returns a Flask Response object containing the
    JSON data with UTF-8 encoding, with the deleted
    book data... or an error message.
    """
    # Find the book with the given ID
    book = _find_book_by_id(book_id)

    # If the book wasn't found, return a 404 error
    if book is None:
        return '', 404

    # Remove the book from the list
    books.remove(book)

    # Update the database
    database.save_posts_to_json(books)

    # Return the deleted book
    return _jsonify_tilde(book)


##  Error Handling

@app.errorhandler(404)
def not_found_error(error) -> Response:
    """
    Handles 404 Not Found errors.
    """
    return jsonify({"error": "Not Found"}), 404


@app.errorhandler(405)
def method_not_allowed_error(error) -> Response:
    """
    Handles 405 Method Not Allowed errors.
    """
    return jsonify({"error": "Method Not Allowed"}), 405


if __name__ == "__main__":
    file_path = os.path.join('data', 'books.json')
    database = HandleJson(file_path)
    books = database.load_posts_from_json()

    webbrowser.open_new("http://127.0.0.1:5001/api/books")
    app.run(host="0.0.0.0", port=5001, debug=True)
