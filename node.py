import datetime
import time

from flask import Flask, request, Response

app = Flask(__name__)

C2_ADDRESS = None
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


@app.route('/set_C2_address', methods=['GET'])
def set_C2_address():
    global C2_ADDRESS
    if C2_ADDRESS is None:
        C2_ADDRESS = request.remote_addr
        return Response(status=200)
    else:
        return Response(status=403)


if __name__ == '__main__':
    start = time.time()
    app.run(host="0.0.0.0", port=80)
