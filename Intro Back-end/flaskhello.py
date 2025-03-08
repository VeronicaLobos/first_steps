from flask import Flask, request
from datetime import datetime
import webbrowser

app = Flask(__name__)

LANDING_PAGE = """<html><head>
    <title>My Landing Page</title></head><body>
    <div align="center">
    <h1>Hello, {0}!</h1>
    <p>The time is {1}.</p><br>
    <img src="https://www.google.com/images/logo.png"><br><br>
    <form action="https://google.com/search" method="get">
    Enter your search words: <input type="text" name="q"><br><br>
    <input type="submit" name="btnG" value="Google Search">
    </form></div>
    <h2>Welcome to the Greeter</h2>
    <form action="/greet">
    What's your name? <input type='text' name='username'><br>
    What's your favorite food? <input type='text' name='favfood'><br>
    <input type='submit' value='Continue'></form>
    </body></html>"""

GREET_HTML = """
    <html><body>
    <h2>Hello, {0}!</h2>
    <p>{1}</p>
    </body></html>
    """


@app.route('/')
def home():
    try:
        name = request.args['name']
        return LANDING_PAGE.format(name, str(datetime.now()))
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


@app.route('/greet')
def greet():
    username = request.args.get('username', '')
    favfood = request.args.get('favfood', '')
    if username == '':
        username = 'World'
    if favfood == '':
        msg = 'You did not tell me your favorite food.'
    else:
        msg = f'I like {favfood}, too.'

    return GREET_HTML.format(username, msg)


""" 
@app.route('/file/<filename>')
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        #render an html template instead of a plain message.
        return render_template('file_not_found.html', filename=filename)
    except Exception as e:
        return f"File error: {str(e)}"
"""


if __name__ == "__main__":
    # Automatically opens the Flask's application website
    # in a browser when the server starts
    url = 'http://127.0.0.1:5001/?name=Veronica'
    webbrowser.open_new(url)
    # Launches the Flask dev server
    app.run(host="0.0.0.0", port=5001, debug=True)