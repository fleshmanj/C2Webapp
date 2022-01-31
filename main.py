# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import time

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
    while True:
        current_time = time.time()
        previous_time = None
        if current_time != previous_time:
            previous_time = current_time
            return str(previous_time)

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

def timer():
    while True:
        current_time = time.localtime(time.time())
        previous_time = None
        if current_time != previous_time:
            previous_time = current_time
        print(previous_time)


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
    timer()