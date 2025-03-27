# My first RESTful API (for Managing Books)

This project showcases a basic RESTful API built with Flask, designed to manage a collection of books. It serves as an educational example and can be extended for more complex applications, and as a playground to learn how to test with Postman.  

It provides endpoints for retrieving, adding, updating, and deleting book records. The API uses a JSON file (`books.json`) as its data store.

<img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/python.png" alt="Python" title="Python"/>
<img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/flask.png" alt="Flask" title="Flask"/>
<img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/rest.png" alt="REST" title="REST"/>
<img width="50" src="https://raw.githubusercontent.com/marwin1991/profile-technology-icons/refs/heads/main/icons/postman.png" alt="Postman" title="Postman"/>


## Features

* **GET /api/books:** Retrieve all books, filter by author, or paginate results.
* **POST /api/books:** Add a new book to the collection.
* **PUT /api/books/<id>:** Update an existing book by its ID.
* **DELETE /api/books/<id>:** Delete a book by its ID.
* **Data Validation:** Ensures that new books have the required fields (title and author).
* **Rate Limiting:** Limits requests to 10 per minute to prevent abuse.
* **Error Handling:** Returns appropriate HTTP status codes and error messages for invalid requests or missing resources.
* **UTF-8 Support:** Handles non-ASCII characters in book titles and author names.
* **JSON Database:** Uses a JSON file to store the book data.
* **Pagination:** Allows to retrieve books in pages.
* **Filtering:** Allows to retrieve books by author.
* **Logging:** Logs informational messages about incoming requests and other relevant events to the console.

## File Structure

RESTful API/  
├──app_first_api.py # Main Flask application file  
├── data/  
│ └── books.json # JSON file storing book data  
├── handle_json.py # Module for reading/writing to the JSON database  
├── data_fetcher.py # Example script to interact with the API  
├── requests_get_demo.py # Example script to interact with a web page  
├── README.md # You are here
└── requisites.txt # Dependencies

## Prerequisites

*   **Python 3.x:** Make sure you have Python 3 installed on your system.
*   **Virtual Environment (Recommended):**  
    ```bash
    # Create a virtual environment named 'venv'
    python3 -m venv venv
    ```
    Linux/macOS:
    ```bash
    # Activate the virtual environment (Linux/macOS)
    source venv/bin/activate
    ```
    Windows:
    ```bash
    # Activate the virtual environment (Windows)
    venv\Scripts\activate
    ```
*   **Flask:** Install Flask using pip:  
    ```bash
    pip install Flask
*   **Flask-Limiter:** Install Flask-Limiter for rate limiting:  
    ```bash
    pip install Flask-Limiter  
*   **Requests:** Install requests for the `data_fetcher.py` and `requests_get_demo.py` scripts:  
    ```bash
    pip install requests

## Setup and Running the API

1.  **Clone the repository:** (If you have this project in a git repository)
    ```bash
    git clone <repository_url>
    cd RESTful API
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd RESTful API
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Flask application:**
    ```bash
    python app_first_api.py
    ```
    This will start the Flask development server. The API will be accessible at `http://127.0.0.1:5001/api/books`. The app will also open the url in your default browser.
    The Port is set to 5001 for Mac User, but you can set it to 5000 as default.

## Using the API

Here are some examples of how to interact with the API using `curl`, `data_fetcher.py`, or Postman:

### Interacting with `curl` (Command Line)

#### GET /api/books

*   **Get all books:**
    ```bash curl http://127.0.0.1:5001/api/books```
*   **Get books by author:**
    ```bash curl "http://127.0.0.1:5001/api/books?author=J.R.R.+Tolkien"```
*   **Get paginated books (page 2, limit 5):**
    ```bash curl "http://127.0.0.1:5001/api/books?page=2&limit=5"```
*   **Get paginated books using data_fetcher.py:**
    ```bash python data_fetcher.py```
    This script will fetch all the books in pages of 5.

#### POST /api/books

*   **Add a new book:**
    ```bash curl -X POST -H "Content-Type: application/json" -d '{"title": "New Book", "author": "New Author"}' http://127.0.0.1:5001/api/books```

#### PUT /api/books/<id>

*   **Update a book (e.g., book with ID 1):**
    ```bash curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Book"}```

#### DELETE /api/books/<id>

*   **Delete a book (e.g., book with ID 1):**
    ```bash curl -X DELETE http://127.0.0.1:5001/api/books/1```


### Interacting with Postman

Postman is a powerful tool for testing APIs. Here's how you can use it with this project:

1.  **Start the API:** Run `python app_first_api.py` in your terminal.
2.  **Open Postman:** Launch the Postman application.
3.  **Create Requests:**
    *   **GET /api/books:**
        *   Select `GET` as the HTTP method.
        *   Enter `http://127.0.0.1:5001/api/books` as the URL.
        *   Click "Send".
    *   **GET /api/books?author=...:**
        *   Select `GET` as the HTTP method.
        *   Enter `http://127.0.0.1:5001/api/books` as the URL.
        *   Go to the "Params" tab and add a `key` named `author` and a `value` (e.g., `J.R.R. Tolkien`).
        *   Click "Send".
    *   **GET /api/books?page=...&limit=...:**
        *   Select `GET` as the HTTP method.
        *   Enter `http://127.0.0.1:5001/api/books` as the URL.
        *   Go to the "Params" tab and add `page` and `limit` keys with their respective values.
        *   Click "Send".
    *   **POST /api/books:**
        *   Select `POST` as the HTTP method.
        *   Enter `http://127.0.0.1:5001/api/books` as the URL.
        *   Go to the "Body" tab, select "raw", and choose "JSON" from the dropdown.
        *   Enter the JSON data (e.g., `{"title": "New Book", "author": "New Author"}`).
        *   Click "Send".
    *   **PUT /api/books/<id>:**
        *   Select `PUT` as the HTTP method.
        *   Enter `http://127.0.0.1:5001/api/books/1` (replace `1` with the book ID) as the URL.
        *   Go to the "Body" tab, select "raw", and choose "JSON" from the dropdown.
        *   Enter the JSON data (e.g., `{"title": "Updated Title"}`).
        *   Click "Send".
    *   **DELETE /api/books/<id>:**
        *   Select `DELETE` as the HTTP method.
        *   Enter `http://127.0.0.1:5001/api/books/1` (replace `1` with the book ID) as the URL.
        *   Click "Send".

## Error Handling

The API returns appropriate HTTP status codes and error messages:

*   **400 Bad Request:** For invalid book data in POST requests.
*   **404 Not Found:** If a book with the specified ID is not found or if no books are found for a given author.
*   **405 Method Not Allowed:** If an unsupported HTTP method is used for an endpoint.
*   **429 Too Many Requests:** If the rate limit is exceeded.

## `data_fetcher.py`

The `data_fetcher.py` script demonstrates how to interact with the API to retrieve books in a loop, fetching a specified number of books per page. It's designed to work with the API running on Codio, but you can adapt it to work locally.

## Contributing

If you'd like to contribute to this project, please feel free to open a pull request.

## License

None