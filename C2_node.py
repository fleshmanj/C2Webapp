# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import datetime
import time
import argparse

from flask import Flask, redirect, url_for, request, render_template, Response

app = Flask(__name__)

C2_ADDRESS = None
node_list = []


@app.route('/')
def index():
    return Response(status=200)

@app.route('/status', methods=['GET'])
def get_status():
    global running
    if running is not None:
        if running:
            return Response(status=200)
        else:
            return Response(status=403)
    else:
        return Response(status=400)


@app.route('/start', methods=['GET'])
def start():
    global running
    if running is None:
        running = True
        return Response(status=200)
    if running:
        return Response(status=403)
    else:
        running = True
        return Response(status=200)

@app.route('/stop', methods=['GET'])
def stop():
    global running
    if running is None:
        return Response(status=403)
    if running:
        running = False
        return Response(status=200)
    else:
        return Response(status=403)


@app.route('/uptime', methods=['GET'])
def uptime():
    global start
    sdt = datetime.datetime.fromtimestamp(start)
    ndt = datetime.datetime.now()
    if request.method == 'GET':
        return f"Server runtime is {ndt - sdt}."



# main driver function
if __name__ == '__main__':
    start = time.time()
    app.run(debug=True, host="0.0.0.0", port=80)
