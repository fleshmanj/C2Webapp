# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, url_for, request, render_template

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'This is my Main computer'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


@app.route('/fu')
def fu():
    return "FU"


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')


class Node():

    def __init__(self, C2_address="0.0.0.0", port=80):
        self.id = None
        self.port = port
        self.C2_address = C2_address

    @app.route('/id')
    def show_id(self):
        return self.id


    def set_id(self, id):
        self.id = id


    @app.route('/set_id/<id>')
    def success(self, id):
        self.set_id(id)
        return 'welcome %s' % id


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    client = Node()
    app.run(debug=True, host="0.0.0.0", port=80)
