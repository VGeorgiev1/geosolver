from flask import Flask, render_template, request,jsonify, redirect, url_for
app = Flask(__name__)
import json
# result = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/points', methods=['GET', 'POST'])
def points():
    print('hello')
    if request.method == 'POST':
        return json.dumps(request.form)
   
if __name__ == '__main__':
    app.run()