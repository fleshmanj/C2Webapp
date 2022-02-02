import datetime
import time
import argparse
import requests
from flask import Flask, request, render_template, Response

app = Flask(__name__)

C2_ADDRESS = None
node_list = []


class Node:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port


@app.route('/', methods=['GET'])
def index():
    statuses = []
    for n in node_list:
        data = requests.get(f"http://{n.ip}:{n.port}/status")
        statuses.append(data.status_code)
    return str(statuses)


@app.route('/start', methods=['GET'])
def start():
    global node_list
    for n in node_list:
        data = requests.get(f"http://{n.ip}:{n.port}/start")
    return Response(status=200)


@app.route('/stop', methods=['GET'])
def stop():
    global node_list
    for n in node_list:
        data = requests.get(f"http://{n.ip}:{n.port}/stop")
    return Response(status=200)


def initial():
    global node_list
    for n in node_list:
        requests.get(f"http://{n.ip}:{n.port}/set_C2_address")


if __name__ == '__main__':
    start = time.time()
    l = Node("laptop", '192.168.1.1', 80)
    node_list.append(l)
    p = Node("pi", "192.168.1.1", 80)
    node_list.append(p)
    initial()
    app.run(host="0.0.0.0", port=80)
