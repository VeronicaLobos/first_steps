from flask import Flask, jsonify, request
import webbrowser

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

##  Data Validation

def validate_book_data(data):
    if "title" not in data or "author" not in data:
        return False
    return True


@app.route('/api/books', methods=['GET', 'POST'])
def handle_books():
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
            return jsonify(filtered_books)
        else:
            return jsonify(books)


def find_book_by_id(book_id):
  """ Find the book with the id `book_id`.
  If there is no book with this id, return None. """
  book = [book for book in books if book['id'] == book_id]
  if len(book) == 0:
    return None
  return book[0]


@app.route('/api/books/<int:id>', methods=['PUT'])
def handle_book(id):
    # Find the book with the given ID
    book = find_book_by_id(id)

    # If the book wasn't found, return a 404 error
    if book is None:
        return '', 404

    # Update the book with the new data
    new_data = request.get_json()
    book.update(new_data)

    # Return the updated book
    return jsonify(book)


@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    # Find the book with the given ID
    book = find_book_by_id(id)

    # If the book wasn't found, return a 404 error
    if book is None:
        return '', 404

    # Remove the book from the list
    books.remove(book)

    # Return the deleted book
    return jsonify(book)


##  Error Handling

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not Found"}), 404


@app.errorhandler(405)
def method_not_allowed_error(error):
    return jsonify({"error": "Method Not Allowed"}), 405


if __name__ == "__main__":
    webbrowser.open_new("http://127.0.0.1:5001/api/books")
    app.run(host="0.0.0.0", port=5001, debug=True)
