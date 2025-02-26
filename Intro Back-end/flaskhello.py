from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    return """<html><head>
    <title>My Landing Page</title></head><body>
    <div align="center"><h1>Hello, world!</h1>
    <p>The time is """ + str(datetime.now()) + """.</p><br>
    <img src="https://www.google.com/images/logo.png"><br><br>
    <form action="https://google.com/search" method="get">
    Enter your search words: <input type="text" name="q"><br><br>
    <input type="submit" name="btnG" value="Google Search">
    </form></div></body></html>"""


if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="0.0.0.0", port=5001, debug=True)