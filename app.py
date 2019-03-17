from flask import Flask, render_template, request,jsonify, redirect, url_for
from eval import eval

app = Flask(__name__)
import json
# result = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/points', methods=['GET', 'POST'])
def points():
    if request.method == 'POST':
        return json.dumps(request.json)

@app.route('/code', methods=['GET', 'POST'])
def code():
    codee = request.json['code']
    print(eval(codee))
    if request.method == 'POST':
        return 'asd'

if __name__ == '__main__':
    app.debug = True
    app.run(port=8181)