"""
Small practice to learn about Flask, jinja2 and
HTML templates.
It this case, the data from a dictionary is rendered
with a loop in jinja2 as a bullet list.
Then, conditionals are added.
Finally, the data is rendered as a table.
"""

from flask import Flask, render_template
import webbrowser

app = Flask(__name__)

"""
Exercises

1. More Details
Change the index.html template to display additional 
information based on the name of the user.
Added country flag emoji.
"""

users = {
    "Alice": {"age": 30, "country": "USA", "flag": "🇺🇸"},
    "Bob": {"age": 25, "country": "Canada", "flag": "🇨🇦"},
    "Charlie": {"age": 35, "country": "UK", "flag": "🇬🇧"},
}


@app.route('/loop')
def loop():
    return render_template('users_details.html',
                           title="Users details", users=users)

"""
2. List of Users
Add an additional template and and additional route 
called /all-users. When browsing to this URL, a list 
of all the users should be displayed along with their 
information.

3. Bonus - Table
Read about tables in HTML, and implement the previous 
step with a table. I.e., a table of users should be 
displayed.
"""


@app.route('/all_users')
def table_contents():
    return render_template('users_det_table.html',
                           title="Users table", users=users)


if __name__ == '__main__':
    url_loop = 'http://127.0.0.1:5001/loop'
    url_table = 'http://127.0.0.1:5001/all_users'
    webbrowser.open_new(url_table)
    app.run(host='0.0.0.0', port=5001, debug=True)
