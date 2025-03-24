from flask import Flask, render_template, request
import webbrowser


app = Flask(__name__)

"""
A GET request is used to retrieve data from a server. 
This is the default HTTP method for Flask routes. 
When you visit a website in your browser, you’re making a 
GET request.
"""

@app.route('/user/<name>', methods=['GET'])
def get_name(name):
    return render_template('index.html', title='Home', user=name)

"""
A POST request is used to send data to the server, for example,
 when you submit a form. Flask can handle POST requests and 
 retrieve the data sent by the client.
"""

@app.route('/update_profile', methods=['GET', 'POST'])
def user_info():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        ## return f"Updating profile of {username} with email {email}"
        return render_template('post_index.html', username=username, email=email)
    return render_template('post_form.html')


if __name__ == "__main__":
    webbrowser.open_new_tab("http://192.168.2.104:5001/update_profile")
    app.run(host="0.0.0.0", port=5001, debug=True)
