from flask import Flask, render_template, request,jsonify, redirect, url_for
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
    if request.method == 'POST':
        pass
if __name__ == '__main__':
    app.debug = True
    app.run(port=8080)