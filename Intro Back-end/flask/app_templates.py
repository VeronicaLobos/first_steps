"""
Small practice to learn about Flask, jinja2 and HTML templates.
"""

from flask import Flask, render_template, request
from datetime import datetime
import webbrowser

app = Flask(__name__, template_folder = 'templates')

ERROR_404 = """
    <html><body>
    <p>Error 404: File not found</p>
    </body></html>
    """

"""
Exercises

1. Add another variable
Change the HTML template so it displays the current time 
when the user access the page. You can choose how it is 
displayed in the HTML.

2. Get name from a GET parameter
Currently, the name is hardcoded “Alice” in the code. 
We want the name to be retrieved from a GET parameter.
"""

@app.route('/')
def index():
    time = str(datetime.now())
    try:
        title = "Home"
        user = request.args['name']
        return render_template('index.html', title=title, user=user, time=time)
    except FileNotFoundError:
        return ERROR_404
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


"""
3. Create a form
Add another template file under templates folder, 
call it form.html or whatever name you want.
"""

@app.route('/form')
def greeter_form():
    return render_template('greeter_form.html')


@app.route('/googleform')
def google_form():
    return render_template('google_form.html')


if __name__ == "__main__":
    url = 'http://127.0.0.1:5001/?name=Veronica'
    url3 = 'http://127.0.0.1:5001/form'
    webbrowser.open_new(url3)
    app.run(host='0.0.0.0', port=5001, debug=True)
