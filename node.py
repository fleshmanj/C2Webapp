# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import datetime
import time
import argparse
import requests as r

from flask import Flask, redirect, url_for, request, render_template, Response

parser = argparse.ArgumentParser(description='Creates a client Node that reports back to the C2 Node.')
parser.add_argument("-i", "--ip", type=str, help='IP address for C2 node', default="0.0.0.0")
args = parser.parse_args()

app = Flask(__name__)

C2_ADDRESS = args.ip
running = None


@app.route('/status', methods=['GET'])
def status():
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


# @app.route('/C2_address', methods=['GET'])
# def C2_address():
#     global C2_ADDRESS
#     if C2_ADDRESS is None:
#         return render_template("C2_address.html")
#     else:
#         return Response(status=403)
#
#
# @app.route('/set_C2_address', methods=['POST'])
# def set_C2_address():
#     global C2_ADDRESS
#     if C2_ADDRESS is None:
#         C2_ADDRESS = request.form['C2address']
#         return Response(status=200)
#     else:
#         return Response(status=403)

def ping_C2():
    global C2_ADDRESS
    temp = r.get(f"https://{C2_ADDRESS}").status_code == 200
    print(f"Up status is {temp}")



# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.

    start = time.time()
    app.run(debug=True, host="0.0.0.0", port=80)
    ping_C2()

