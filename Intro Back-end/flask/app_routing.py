from flask import Flask, render_template, request
import webbrowser


app = Flask(__name__)

"""
Flask routes can also contain variable sections, 
which can be used to capture dynamic values from the URL.
The variable can be then passed to a template.
"""


@app.route('/')
def handle_params():
    name = request.args.get('name', 'Guest')
    return render_template('simple_index.html', title='Home', user=name)

"""
Exercise

Change your code to greet the user based on the name
provided in the URL.
"""


@app.route('/<name>')
def greet(name):  # changed to name
    return render_template('simple_index.html', title='Home', user=name)


@app.route('/user/<name>', methods=['GET'])
def get_name(name):
    return render_template('index.html', title='Home', user=name)


if __name__ == "__main__":
    webbrowser.open_new_tab("http://192.168.2.104:5001/?name=Alice")
    webbrowser.open_new_tab("http://192.168.2.104:5001/Alice")
    webbrowser.open_new_tab("http://192.168.2.104:5001/user/Alice")
    app.run(host="0.0.0.0", port=5001, debug=True)
