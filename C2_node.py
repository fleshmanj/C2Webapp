# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import datetime
import time
import argparse

from flask import Flask, redirect, url_for, request, render_template, Response

app = Flask(__name__)

C2_ADDRESS = args.ip
node_list = []



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
    parser = argparse.ArgumentParser(description='Creates a client Node that reports back to the C2 Node.')
    parser.add_argument("-i", "--ip", type=str, help='IP address for C2 node', default="0.0.0.0")
    start = time.time()
    app.run(debug=True, host="0.0.0.0", port=80)
