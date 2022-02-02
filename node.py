from flask import Flask, redirect, url_for, request, render_template
import time
import datetime

app = Flask(__name__)


@app.route('/uptime')
def uptime():
    global start
    sdt = datetime.datetime.fromtimestamp(start)
    ndt = datetime.datetime.now()
    return f"Server has been up for {ndt - sdt}"


start = time.time()
app.run(debug=True, host="0.0.0.0", port=80)
