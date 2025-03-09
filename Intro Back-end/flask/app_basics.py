from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/')
def index():
    ## Returns static content
    ## curl http://127.0.0.1:5001
    ## Returns Status Header
    ## curl -I http://127.0.0.1:5001
    response = make_response('<h1>Hello, World!</h1>\n')
    response.status_code = 201
    response.headers['Custom-header'] = ':) hey there'
    return response


"""
Returns static content
"""
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    ##  Serves the html file
    ##  curl http://127.0.0.1:5001/hello
    if request.method == 'GET':
        return "You made a GET request!\n"
    ##  Processes the information from a form
    ##  curl -X POST http://127.0.0.1:5001/hello
    elif request.method == 'POST':
        return "You made a POST request!\n"


"""
URL processor, with a dynamic variable
curl http://127.0.0.1:5001/greet/World
"""
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!\n"


"""
URL processor, simple calculator
curl http://127.0.0.1:5001/add/1/2
"""
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}\n"


"""
URL processor with request function
http://127.0.0.1:5001/handle_url_params?greeting=Hello&name=World
"""
@app.route('/handle_url_params')
def handle_params():
    greeting = request.args.get('greeting')
    name = request.args.get('name')
    return f'{greeting}, {name}!'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
