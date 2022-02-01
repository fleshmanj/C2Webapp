# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import datetime
import time

from flask import Flask, redirect, url_for, request, render_template, Response




# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

C2_ADDRESS = None

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


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')

@app.route('/id')
def show_id():
    return

@app.route('/set_id/<id>')
def set_id(id):
    return 'welcome %s' % id


@app.route('/uptime', methods=['GET'])
def uptime():
    global start
    sdt = datetime.datetime.fromtimestamp(start)
    ndt = datetime.datetime.now()
    if request.method == 'GET':
        return f"Server runtime is {ndt - sdt}."


@app.route('/set_C2_address/<address>', methods=['POST'])
def set_C2_address(address):
    global C2_ADDRESS
    if C2_ADDRESS is None:
        C2_ADDRESS = address
        return Response(status=200)
    else:
        return Response(status=403)




# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    start = time.time()
    app.run(debug=True, host="0.0.0.0", port=80)
